# 📊 Accounting App

A full-stack accounting application for managing invoices, expenses, income, and financial reports. Built with a FastAPI backend and a Streamlit frontend.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)

## 🎯 The Business Problem

Most small-to-medium businesses use spreadsheets to track their accounting, which leads to version control issues, lack of security, and manual data entry. 

I built this application to demonstrate how to create a secure, centralized backend for financial data. It uses a multi-tenant architecture, meaning it can securely handle data for multiple different companies without ever mixing their financial records.

## 📖 Features

- ✅ **User Authentication:** Secure JWT-based login and registration.
- ✅ **Multi-Tenancy:** Data isolation ensures users only see their own company's data.
- ✅ **Invoice Management:** Create, read, update, and delete invoices.
- ✅ **Expense & Income Tracking:** Log and categorize cash flow.
- ✅ **Financial Reports:** Generate summary data.
- ✅ **Interactive Dashboard:** Visualize data using Streamlit and Plotly.

## 🚀 Tech Stack

### Backend (API)
- **FastAPI** - High-performance web framework for building APIs.
- **SQLAlchemy** - ORM for database operations.
- **SQLite** - Lightweight relational database for development.
- **Pydantic** - Data validation and settings management.
- **Pytest** - Automated testing with in-memory DB isolation.

### Frontend (UI)
- **Streamlit** - Python-based web framework for rapid UI development.
- **Pandas** - Data manipulation.
- **Plotly** - Interactive charts and dashboards.

## 📂 Project Structure

```text
accounting-app/
├── app/
│   ├── api/          # API endpoints (auth, invoices, accounts, etc.)
│   ├── core/         # Configuration and security (JWT)
│   ├── models/       # SQLAlchemy database models
│   ├── schemas/      # Pydantic validation schemas
│   ├── services/     # Business logic
│   └── frontend.py   # Streamlit dashboard
├── tests/            # Pytest suite (conftest.py + route tests)
├── requirements.txt
└── .env.example
