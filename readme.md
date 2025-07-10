
---

### 📄 `README.md`

```markdown
# BiometricsTracking API

This is a FastAPI application that connects to a MySQL database and exposes RESTful endpoints to:

- List all tables in the database
- Retrieve the first 100 rows from any specified table

## 📦 Requirements

- Python 3.8+
- MySQL database access credentials

## 🔧 Installation

1. Clone or download this project.
2. Navigate to the project directory.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the API

Start the FastAPI server with:

```bash
uvicorn main_sanitized:app --reload
```

Then open your browser and go to:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 🔗 API Endpoints

| Method | Endpoint              | Description                          |
|--------|-----------------------|--------------------------------------|
| GET    | `/`                   | Welcome message                      |
| GET    | `/tables`             | Lists all tables in the database     |
| GET    | `/data/{table_name}`  | Returns first 100 rows from a table  |

## 🛡️ Security

Make sure to replace `<your-database-host>`, `<your-username>`, and `<your-password>` in `main_sanitized.py` with your actual credentials before running the app.
```

---

### 📄 `requirements.txt`

```txt
fastapi
uvicorn
mysql-connector-python
```

---

Would you like me to generate these as downloadable files now?