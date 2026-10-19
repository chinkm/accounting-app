import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.database import get_db
from app.models import Base
from main import app

# Create an isolated test SQLite database for testing
# In-memory SQLite engine - the database
# Note: StaticPool keeps the same connection open for the duration of the test session, which is necessary for in-memory SQLite databases.
# Without it, the database would be lost after each connection is closed.
TEST_DATABASE_URL = "sqlite://"
engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(autouse=True, scope="function")
def setup_database():
    # Create the database tables before each test
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after tests are done
    Base.metadata.drop_all(bind=engine)


def override_get_db():
    """Override the get_db dependency to use the test database session."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client(setup_database):
    """Create a test client for the FastAPI app."""
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()  # Clear overrides after the test


@pytest.fixture
def db_session():
    """Yield a database session for testing."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()
