def create_author(client, name="Autor1"):
    response = client.post("/authors/", json={"name": name})
    assert response.status_code == 200
    return response.json()["id"]


def create_user(client, name="Maria", email="maria@email.com"):
    response = client.post("/users/", json={"name": name, "email": email})
    assert response.status_code == 200
    return response.json()["id"]

def create_loan(client, user_id, book_id):
    response = client.post("/loans/", json={"user_id": user_id, "book_id": book_id})
    assert response.status_code == 200
    return response.json()["id"]

def return_loan(client, loan_id):
    response = client.post(f"/loans/{loan_id}/return")
    assert response.status_code == 200
    return response.json()


def test_fine_calculation(client):
    user_id = create_user(client)
    loan_id = create_loan(client, user_id, book_id=1)

    data = return_loan(client, loan_id)

    assert "fine_amount" in data
    assert data["fine_amount"] >= 0