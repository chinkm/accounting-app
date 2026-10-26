import uuid


def test_get_accounts_without_token_returns_401(client):
    response = client.get("/api/accounts/")
    assert response.status_code == 401


def test_register_login_create_account(client):
    unique_email = f"test_{uuid.uuid4().hex[:8]}@example.com"
    # Register a new user
    response = client.post(
        "/api/auth/register",
        json={
            "name": "Test User7",
            "email": unique_email,
            "role": "user",
            "password": "testpass123",
            "company_id": 3,
        },
    )

    assert response.status_code == 201

    # Login with the new user
    response = client.post(
        "/api/auth/login",
        data={"username": unique_email, "password": "testpass123"},
    )

    assert response.status_code == 200
    token = response.json()["access_token"]

    # Create an account for the user
    response = client.post(
        "/api/accounts/",
        json={"company_id": 3, "name": "Test Bank5", "type": "bank", "balance": 0},
        headers={"Authorization": f"Bearer {token}"},
    )
    print(response.json())
    assert response.status_code == 201
    assert response.json()["name"] == "Test Bank5"
