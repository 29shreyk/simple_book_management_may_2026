from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)
CORS(app)
app.config["JWT_SECRET_KEY"] = "demo"
jwt = JWTManager(app)

DB_PATH = os.path.join(os.path.dirname(__file__), 'books.db')

def get_db_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            publisher TEXT NOT NULL,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            Cost REAL NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

@app.route('/', methods=['GET'])
@jwt_required()
def get_books():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify([dict(row) for row in rows])


@app.route('/create', methods=['POST'])
@jwt_required()
def create_books():
    new_book = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO book (publisher, name, date, Cost) VALUES (?, ?, ?, ?)",
        (new_book['publisher'], new_book['name'], new_book['date'], new_book['Cost'])
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(new_book), 201


@app.route('/update/<int:id>', methods=['PUT'])
@jwt_required()
def update_book(id):
    updated_book = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE book SET publisher=?, name=?, date=?, Cost=? WHERE id=?",
        (updated_book['publisher'], updated_book['name'], updated_book['date'], updated_book['Cost'], id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(updated_book)


@app.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book WHERE id=?", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'result': 'Book deleted'})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400

    hashed_password = generate_password_hash(password)

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': 'Username already exists'}), 409


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    if not user or not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5001)
