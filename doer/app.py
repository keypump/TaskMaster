from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# -----------------------------
# Database connection
# -----------------------------
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "task_vault"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    return conn

# -----------------------------
# Initialize DB table if missing
# -----------------------------
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            description TEXT NOT NULL,
            status VARCHAR(20) DEFAULT 'pending'
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# -----------------------------
# Flask Routes
# -----------------------------
@app.route("/")
def home():
    return jsonify({"message": "Welcome to TaskMaster! Let's get your tasks done and stay productive."})

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    description = data.get("description")
    status = data.get("status", "pending")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (description, status) VALUES (%s, %s) RETURNING id;",
        (description, status)
    )
    task_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"id": task_id, "description": description, "status": status})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, description, status FROM tasks;")
    tasks = [{"id": t[0], "description": t[1], "status": t[2]} for t in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify({"tasks": tasks})

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    description = data.get("description")
    status = data.get("status")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE tasks SET description=%s, status=%s WHERE id=%s;",
        (description, status, task_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": f"Task {task_id} updated successfully"})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=%s;", (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": f"Task {task_id} deleted successfully"})

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    # Initialize the tasks table on startup
    init_db()
    app.run(host="0.0.0.0", port=5000)