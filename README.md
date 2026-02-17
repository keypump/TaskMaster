# TaskMaster 🚀

## Overview
TaskMaster is a Dockerized To-Do application demonstrating Docker fundamentals.  
It includes a Flask backend (`doer`) and a PostgreSQL database (`task_vault`) with persistent storage.

## Features
- Create, read, update, and delete tasks (CRUD)
- Flask app is containerized
- PostgreSQL container with persistent volume
- Custom Docker network for container communication
- Environment variables for configuration
- Motivational messages in the API responses to make the project fun to do 

## Setup

1. Clone the repo:
```bash
git clone https://github.com/keypump/TaskMaster.git
cd TaskMaster


2. Set environment variables:
```bash
cp .env.example .env


3. Start containers:
```bash
docker compose up -d..


4.	Check containers:
```bash
docker ps

5.	Test API:
```bash
curl http://localhost:5000/



Architecture
•	doer: Flask app handling tasks
•	task_vault: PostgreSQL database storing tasks
•	vault_data: volume for persistent storage
•	task_network: network for communication



Naming & Theme
•	TaskMaster: main project
•	doer: Flask app / “engine” of TaskMaster
•	task_vault: PostgreSQL container / “treasure chest” of tasks
•	task_network: custom network
•	vault_data: persistent storage
    
Lessons Learned
•	Using standard PostgreSQL env vars simplifies setup
•	Docker volumes for persistence
•	Full CRUD implementation with Flask
•	Adding personality makes APIs more engaging





