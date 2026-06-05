import pytest
import json

def test_get_books_returns_list(client, auth_headers):
    response = client.get("/", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_create_valid_book(client, auth_headers):
    payload = {
        "publisher": "O'Reilly",
        "name": "Learning Flask",
        "date": "2024-10-11",
        "Cost": 399.99
    }
    response = client.post("/create", json=payload, headers=auth_headers)
    assert response.status_code == 201

def test_create_book_returns_correct_name(client, auth_headers):
    payload = {
        "publisher": "Packt",
        "name": "Python Testing",
        "date": "2024-05-01",
        "Cost": 299.99
    }
    response = client.post("/create", json=payload, headers=auth_headers)
    data = response.get_json()
    assert data["name"] == "Python Testing"

def test_update_existing_book(client, auth_headers):
    payload = {
        "publisher": "OldPub",
        "name": "OldBook",
        "date": "2023-01-01",
        "Cost": 100.0
    }
    create_response = client.post("/create", json=payload, headers=auth_headers)
    assert create_response.status_code == 201

    books = client.get("/", headers=auth_headers).get_json()
    book_id = books[-1]["id"]

    updated_payload = {
        "publisher": "NewPub",
        "name": "NewBook",
        "date": "2025-01-01",
        "Cost": 200.0
    }
    response = client.put(f"/update/{book_id}", json=updated_payload, headers=auth_headers)
    assert response.status_code == 200
    assert response.get_json()["name"] == "NewBook"

def test_delete_existing_book(client, auth_headers):
    payload = {
        "publisher": "DelPub",
        "name": "DeleteMe",
        "date": "2024-01-01",
        "Cost": 50.0
    }
    client.post("/create", json=payload, headers=auth_headers)
    books = client.get("/", headers=auth_headers).get_json()
    book_id = books[-1]["id"]

    response = client.delete(f"/delete/{book_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.get_json()["result"] == "Book deleted"

def test_delete_book_no_longer_exists(client, auth_headers):
    payload = {
        "publisher": "TempPub",
        "name": "TempBook",
        "date": "2024-06-01",
        "Cost": 75.0
    }
    client.post("/create", json=payload, headers=auth_headers)
    books = client.get("/", headers=auth_headers).get_json()
    book_id = books[-1]["id"]
    client.delete(f"/delete/{book_id}", headers=auth_headers)

    books_after = client.get("/", headers=auth_headers).get_json()
    ids = [b["id"] for b in books_after]
    assert book_id not in ids