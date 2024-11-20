from flask import Blueprint, jsonify, abort, request, render_template
from models import db, Book, Order

books_bp = Blueprint('books', __name__)
orders_bp = Blueprint('orders', __name__)

# Маршрут для корневого URL
@books_bp.route('/', methods=['GET'])
def index():
    return "About Books"

# Маршрут для получения всех книг
@books_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

# Маршрут для получения книги по id
@books_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        abort(404)
    return jsonify(book.to_dict())

# Маршрут для оформления заказа
@orders_bp.route('/order', methods=['POST'])
def create_order():
    data = request.json
    if not data or not all(key in data for key in ('first_name', 'last_name', 'phone', 'email', 'book_id')):
        abort(400)

    book_id = data['book_id']
    book = Book.query.get(book_id)
    if book is None:
        abort(404)

    order = Order(
        first_name=data['first_name'],
        last_name=data['last_name'],
        phone=data['phone'],
        email=data['email'],
        book_id=book_id
    )
    db.session.add(order)
    db.session.commit()

    return jsonify(order.to_dict()), 201

# Маршрут для получения всех заказов
@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])
