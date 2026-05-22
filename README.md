# 📊 Accounting App

A modern accounting application for managing invoices, expenses, income, and financial reports.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)

## 📖 Features

- ✅ User Authentication
- ✅ Invoice Management
- ✅ Expense Tracking
- ✅ Income Tracking
- ✅ Financial Reports

## 🚀 Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Lightweight database

### Frontend
- **Streamlit** - Python-based web framework
- **Pandas** - Data manipulation
- **Plotly** - Interactive charts

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/accounting-app.git
cd accounting-app

**Purpose:** Shows people how to get started quickly.

---

### **4. Installation Instructions**

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

**Purpose:** Step-by-step guide to install and set up the app.

---

### **5. Usage Examples**

cp .env.example .env
# Edit .env with your configuration

python -c "from app.database import init_db; init_db()"

# Start the backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Start the frontend
streamlit run app/frontend.py

Frontend: http://localhost:8501
API Docs: http://localhost:8000/docs