
# def test_create_books(client):
#     response = client.post("/authors/", json={"name": "Robert Martin"})
#     assert response.status_code == 200

#     response = client.post("/books/", json={
#         "title": "Clean Code",
#         "author_id": 1,
#         "total_copies": 3
#     })
#     assert response.status_code == 200


    
def test_list_books(client):

    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) > 0