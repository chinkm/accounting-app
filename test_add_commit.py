from app.database import SessionLocal, init_db
from app.models.user import User
from datetime import datetime

# Initialize the database
init_db()

# Create a database session
db = SessionLocal()

# Create a new user
user = User(
    email="john@example.com",
    password_hash="hashed_password",
    name="John Doe",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

# Add the user to the database
db.add(user)
db.commit()
db.refresh(user)

# Print the user ID
print(f"User created with ID: {user.id}")

# Close the database session
db.close()

print("✅ User created successfully!")