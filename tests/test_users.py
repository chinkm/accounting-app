from app.models.user import User
from app.database import SessionLocal


def test_create_and_read_user():
    # Create a new database session
    db = SessionLocal()

    try:
        # Create a new user
        new_user = User(
            name="Test User",
            email="GxuXe@example.com",
            password="password123",
            role="admin",
            company_id=1,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # Read the user from the database
        user = db.query(User).filter(User.email == "GxuXe@example.com").first()

        # Assert that the user was created and read successfully
        assert user is not None
        assert user.name == "Test User"
        assert user.email == "GxuXe@example.com"
        assert user.password == "password123"
        assert user.role == "admin"
        assert user.company_id == 1

    finally:
        db.close()  # Close the database session
