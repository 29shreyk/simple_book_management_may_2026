import pytest
import json

# ----------------------------
# SECTION 1: Get Books
# ----------------------------

def test_get_books_returns_list(client):
    response = client.get("/")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

# ----------------------------
# SECTION 2: Create Book
# ----------------------------

def test_create_valid_book(client):
    payload = {
        "publisher": "O'Reilly",
        "name": "Learning Flask",
        "date": "2024-10-11",
        "Cost": 399.99
    }
    response = client.post("/create", json=payload)
    assert response.status_code == 201

def test_create_book_returns_correct_name(client):
    payload = {
        "publisher": "Packt",
        "name": "Python Testing",
        "date": "2024-05-01",
        "Cost": 299.99
    }
    response = client.post("/create", json=payload)
    data = response.get_json()
    assert data["name"] == "Python Testing"

# ----------------------------
# SECTION 3: Update Book
# ----------------------------

def test_update_existing_book(client):
    # First create a book
    payload = {
        "publisher": "OldPub",
        "name": "OldBook",
        "date": "2023-01-01",
        "Cost": 100.0
    }
    create_response = client.post("/create", json=payload)
    assert create_response.status_code == 201

    # Get all books and find the one we just created
    books = client.get("/").get_json()
    book_id = books[-1]["id"]

    # Now update it
    updated_payload = {
        "publisher": "NewPub",
        "name": "NewBook",
        "date": "2025-01-01",
        "Cost": 200.0
    }
    response = client.put(f"/update/{book_id}", json=updated_payload)
    assert response.status_code == 200
    assert response.get_json()["name"] == "NewBook"

# ----------------------------
# SECTION 4: Delete Book
# ----------------------------

def test_delete_existing_book(client):
    # First create a book to delete
    payload = {
        "publisher": "DelPub",
        "name": "DeleteMe",
        "date": "2024-01-01",
        "Cost": 50.0
    }
    client.post("/create", json=payload)

    # Get its id
    books = client.get("/").get_json()
    book_id = books[-1]["id"]

    # Delete it
    response = client.delete(f"/delete/{book_id}")
    assert response.status_code == 200
    assert response.get_json()["result"] == "Book deleted"

def test_delete_book_no_longer_exists(client):
    # Create and delete a book
    payload = {
        "publisher": "TempPub",
        "name": "TempBook",
        "date": "2024-06-01",
        "Cost": 75.0
    }
    client.post("/create", json=payload)
    books = client.get("/").get_json()
    book_id = books[-1]["id"]
    client.delete(f"/delete/{book_id}")

    # Verify it's gone
    books_after = client.get("/").get_json()
    ids = [b["id"] for b in books_after]
    assert book_id not in ids