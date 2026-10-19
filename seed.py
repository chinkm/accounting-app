# seed.py
from app.database import SessionLocal, engine
from app.models import Base
from sqlalchemy import text

# Assuming Company model is imported like this (adjust path if needed)
from app.models.companies import Company
from app.models.invoice import Invoice
from app.models.expenses import Expense
from app.models.account import Account
from app.models.income import Income
from app.models.transaction import Transaction
from app.models.user import User
from app.models.category import Category


def seed_data():
    print("Connecting to the database...")
    db = SessionLocal()

    try:
        # 1. Double check that tables are built
        Base.metadata.create_all(bind=engine)

        # 2. Check if companies already exist to prevent duplicates
        company_count = db.query(Company).count()
        if company_count > 0:
            print(f"Database already has {company_count} companies. Skipping seeding.")
            return

        print("Seeding initial companies...")

        # 3. Create your group of companies
        golden = Company(name="Golden", email="info@golden.com", address="HQ Office A")
        seroi = Company(name="Seroi", email="info@seroi.com", address="HQ Office B")
        evergreen = Company(
            name="Evergreen", email="info@evergreen.com", address="HQ Office C"
        )

        # 4. Add and commit to database
        db.add_all([golden, seroi, evergreen])
        db.commit()

        print("Successfully seeded companies!")

        # 5. Print out the IDs so you know what numbers to use!
        companies = db.query(Company).all()
        for c in companies:
            print(f"Company Named: '{c.name}' was assigned ID: {c.id}")

    except Exception as e:
        print(f"An error occurred during seeding: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
