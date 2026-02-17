
# 1️⃣ Base Image
FROM python:3.11-slim

# 2️⃣ Set Working Directory
WORKDIR /app

# 3️⃣ Copy Requirements
COPY requirements.txt .

# 4️⃣ Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy Application Code
COPY . .

# 6️⃣ Expose Port
EXPOSE 5000

# 7️⃣ Run Application
CMD ["python", "app.py"]