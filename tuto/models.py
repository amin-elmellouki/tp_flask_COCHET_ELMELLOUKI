from flask_login import UserMixin
from .app import db, login_manager


class favorites(db.Model):
    user_id = db.Column(db.String(50), db.ForeignKey('user.username'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)

class Author (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return self.name

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    title = db.Column(db.String(100))
    url = db.Column(db.String(200))
    img = db.Column(db.String(200))
    author_id = db.Column(db.Integer , db.ForeignKey ("author.id"))
    author = db.relationship ("Author",
        backref=db.backref("books", lazy="dynamic"))
    
    def __repr__(self):
        return "<Book (%d) %s>" % (self.id, self.title)
    
class User(db.Model, UserMixin):
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(64))
    favorite_books = db.relationship('Book', secondary='favorites', backref=db.backref('users_who_favorited', lazy='dynamic'))

    def get_id(self):
        return self.username

def get_book(id):
    return Book.query.get(id)

def get_all_books():
    return Book.query.all()

def get_author(id):
    return Author.query.get(id)

def get_all_authors():
    return Author.query.all()

def get_favorite_books(user):
    return user.favorite_books

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)