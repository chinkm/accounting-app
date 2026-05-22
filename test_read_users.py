from app.database import SessionLocal
from app.models.user import User

# Create a database session
db = SessionLocal()

# Read all users
users = db.query(User).all()

for user in users:
    print(f"ID: {user.id}")
    print(f"Name: {user.name}")
    print(f"Email: {user.email}")
    print("-" * 50)

# Close the database session
db.close()

print("✅ Users read successfully!")