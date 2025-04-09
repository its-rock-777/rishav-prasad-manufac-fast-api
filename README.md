# 🚀 Rishav's FastAPI Assignment Backend

This project is a backend assignment built with **FastAPI**, managed using **Poetry**, and containerized with **Docker**.

---

## 📌 Features

### ✅ API Endpoints

| Method | Route         | Description                                               |
|--------|---------------|-----------------------------------------------------------|
| GET    | `/uuid`       | Returns a new UUIDv4 string on each request               |
| GET    | `/async-uuid` | Same as `/uuid` but with a 3-second async (non-blocking) delay |
| GET    | `/cat`        | Returns a random cat image URL using [cataas](https://cataas.com) |
| POST   | `/upload`     | Upload a CSV file and get row & column stats in response  |

---

## 🧰 Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- Poetry (for dependency management)
- Docker
- uuid module
- httpx (for async API calls)

---

## 🚀 Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/rishav-fastapi-app.git
cd rishav-fastapi-app
