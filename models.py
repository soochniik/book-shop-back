from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    imagebig = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.Text, nullable=False)
    publish = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    series = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    cover = db.Column(db.String(100), nullable=False)
    edition = db.Column(db.Integer, nullable=False)
    age = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'price': self.price,
            'image': self.image,
            'imagebig': self.imagebig,
            'category': self.category,
            'desc': self.desc,
            'publish': self.publish,
            'brand': self.brand,
            'series': self.series,
            'year': self.year,
            'pages': self.pages,
            'cover': self.cover,
            'edition': self.edition,
            'age': self.age
        }

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email,
            'book_id': self.book_id
        }
    