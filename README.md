# 📚 Simple Book Management System (SQLite Edition)

A full-stack Book Management System built using **React (Vite)** for the frontend and **Flask + SQLite** for the backend.

This project allows users to perform complete CRUD operations (Create, Read, Update, Delete) on books through a clean web interface. The application has been enhanced by replacing PostgreSQL with SQLite, making setup significantly easier and eliminating the need for an external database server.

---

## ✨ Features

* Add new books
* View all books
* Update existing books
* Delete books
* RESTful Flask API
* SQLite database integration
* Environment variable based API configuration
* Responsive React frontend
* Automated database initialization
* API testing support with Pytest

---

## 🛠️ Tech Stack

### Frontend

* React
* Vite
* JavaScript
* CSS

### Backend

* Flask
* SQLite3
* Python

### Testing

* Pytest

---

# 📂 Project Structure

```text
simple_book_management_may_2026/
│
├── Client/
│   ├── src/
│   ├── public/
│   ├── .env.example
│   ├── package.json
│   └── vite.config.js
│
├── Server/
│   ├── app.py
│   ├── books.db
│   ├── setup_database.sql
│   ├── Playwright_Test_data.py
│   └── tests/
│       └── pytest/
│
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone Repository

```bash
git clone https://github.com/29shreyk/simple_book_management_may_2026.git

cd simple_book_management_may_2026
```

---

# ⚙️ Backend Setup

Navigate to server directory:

```bash
cd Server
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is unavailable:

```bash
pip install flask flask-cors pytest
```

---

## Run Backend Server

```bash
python app.py
```

Server starts on:

```text
http://localhost:5001
```

### Important

The SQLite database (`books.db`) and required table are automatically created when the server starts for the first time.

No manual database setup is required.

---

# 🎨 Frontend Setup

Open a new terminal.

Navigate to client directory:

```bash
cd Client
```

Install dependencies:

```bash
npm install
```

---

## Configure Environment Variables

Create a `.env` file inside the Client folder.

```env
VITE_API_URL=http://localhost:5001
```

You may also copy from:

```bash
cp .env.example .env
```

or create manually on Windows.

---

## Start Frontend

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

# 🔄 Running the Application

### Terminal 1

```bash
cd Server

python app.py
```

### Terminal 2

```bash
cd Client

npm run dev
```

Open:

```text
http://localhost:5173
```

---

# 📡 API Endpoints

## Get All Books

```http
GET /books
```

---

## Get Book By ID

```http
GET /books/<id>
```

---

## Add Book

```http
POST /books
```

Request Body:

```json
{
  "Title": "Atomic Habits",
  "Author": "James Clear",
  "Genre": "Self Help",
  "Cost": 499
}
```

---

## Update Book

```http
PUT /books/<id>
```

Request Body:

```json
{
  "Title": "Atomic Habits",
  "Author": "James Clear",
  "Genre": "Self Help",
  "Cost": 599
}
```

---

## Delete Book

```http
DELETE /books/<id>
```

---

# 🧪 Running Tests

Navigate to:

```bash
cd Server
```

Run:

```bash
pytest
```

Or:

```bash
pytest tests/pytest
```

---

# 🔥 Improvements Over Original Repository

### Database Migration

* Migrated from PostgreSQL to SQLite.
* Removed dependency on external database servers.
* Simplified setup process.

### Automatic Initialization

* Database creation automated.
* Table creation automated.
* No manual SQL execution required.

### Environment Configuration

* Added Vite environment variable support.
* API URLs are configurable via `.env`.

### Testing Improvements

* Updated test suite for SQLite compatibility.
* Simplified testing workflow.

### Better Developer Experience

* Faster project setup.
* Cross-platform compatibility.
* Reduced installation complexity.

---

# 🧪 API Testing with Pytest

The project includes a Pytest test suite to validate backend API functionality and database operations.

## Prerequisites

Before running tests, ensure all required Python dependencies are installed.

```bash
cd Server

pip install -r requirements.txt
```

or

```bash
pip install pytest flask flask-cors
```

---

## Project Test Structure

```text
Server/
└── tests/
    └── pytest/
        ├── conftest.py
        ├── test_books_api.py
        ├── conftest_postgres_backup.py
        └── test_books_api_backup.py
```

---

## Run All Tests

Navigate to the server directory:

```bash
cd Server
```

Run the complete test suite:

```bash
pytest
```

---

## Run Tests with Verbose Output

```bash
pytest -v
```

Example output:

```text
test_books_api.py::test_get_books PASSED
test_books_api.py::test_create_book PASSED
test_books_api.py::test_update_book PASSED
test_books_api.py::test_delete_book PASSED
```

---

## Run a Specific Test File

```bash
pytest tests/pytest/test_books_api.py
```

---

## Run a Specific Test Case

```bash
pytest tests/pytest/test_books_api.py::test_create_book
```

Example:

```bash
pytest tests/pytest/test_books_api.py::test_get_books
```

---

## Run Tests with Detailed Summary

```bash
pytest -ra
```

---

## Generate Coverage Report (Optional)

Install coverage package:

```bash
pip install pytest-cov
```

Run:

```bash
pytest --cov=.
```

Detailed coverage report:

```bash
pytest --cov=. --cov-report=term-missing
```

---

## What the Tests Validate

The Pytest suite verifies:

### API Functionality

- Fetch all books
- Fetch book by ID
- Create a new book
- Update an existing book
- Delete a book

### Database Operations

- SQLite database connectivity
- Record insertion
- Record updates
- Record deletion
- Data integrity

### Response Validation

- Correct HTTP status codes
- Expected JSON responses
- Proper error handling

---

## Expected Result

A successful test run should produce output similar to:

```text
================== test session starts ==================

collected 4 items

test_books_api.py ....                         [100%]

================== 4 passed in 1.23s ==================
```

---

## Troubleshooting

### ModuleNotFoundError

Ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

---

### Database Errors

Make sure the SQLite database has been initialized by running the Flask server once:

```bash
python app.py
```

---

### Import Errors

Run tests from the Server directory:

```bash
cd Server

pytest
```

instead of running them from the project root.

---

## Recommended Testing Workflow

### 1. Start Backend

```bash
cd Server

python app.py
```

### 2. Run API Tests

```bash
pytest -v
```

### 3. Start Frontend

```bash
cd Client

npm run dev
```

### 4. Run Playwright E2E Tests

```bash
npx playwright test
```

### 5. View Playwright Report

```bash
npx playwright show-report
```

This workflow validates both the backend APIs (Pytest) and the complete user workflow through the browser (Playwright).


# 🎭 End-to-End Testing with Playwright

The project includes Playwright-based end-to-end (E2E) tests to validate the complete workflow of the application through the browser.

## Prerequisites

Make sure both backend and frontend servers are running.

### Terminal 1 - Backend

```bash
cd Server

python app.py
```

Backend should be available at:

```text
http://localhost:5001
```

### Terminal 2 - Frontend

```bash
cd Client

npm install

npm run dev
```

Frontend should be available at:

```text
http://localhost:5173
```

---

## Install Playwright

Navigate to the Playwright test directory (or wherever Playwright is configured).

Install dependencies:

```bash
npm install
```

Install Playwright browsers:

```bash
npx playwright install
```

---

## Generate Sample Test Data (Optional)

The repository includes a utility script for populating the database with sample book records.

```bash
cd Server

python Playwright_Test_data.py
```

This creates test data in the SQLite database that can be used during Playwright test execution.

---

## Run All Playwright Tests

```bash
npx playwright test
```

---

## Run a Specific Test

```bash
npx playwright test <test-file-name>
```

Example:

```bash
npx playwright test book-management.spec.js
```

---

## Run Tests in Headed Mode

To visually watch browser actions:

```bash
npx playwright test --headed
```

---

## Debug Playwright Tests

```bash
npx playwright test --debug
```

This launches Playwright Inspector and allows step-by-step debugging.

---

## View Playwright Test Report

After test execution:

```bash
npx playwright show-report
```

An interactive HTML report will open in your browser.

---

## Playwright Test Coverage

The Playwright suite validates:

- Application launch
- Book creation workflow
- Book update workflow
- Book deletion workflow
- Form validations
- UI interactions
- End-to-end CRUD operations

---

## Recommended Testing Workflow

1. Start Backend Server
2. Start Frontend Server
3. Generate Sample Data (Optional)
4. Run Pytest API Tests
5. Run Playwright E2E Tests
6. Review Playwright HTML Report

```bash
# Backend
cd Server
python app.py

# Frontend
cd Client
npm run dev

# API Tests
pytest

# E2E Tests
npx playwright test

# Report
npx playwright show-report
```


# 📸 Future Enhancements

* Search books by title
* Filter books by genre
* Pagination support
* User authentication
* Book cover image upload
* Docker deployment
* CI/CD integration

---

# 👨‍💻 Author

**Shrey K**

GitHub: https://github.com/29shreyk

---

# 📜 License

This project is intended for educational and learning purposes.
