from .app import app
from flask import render_template
from .models import get_sample
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

@app.route("/")
def home():
    return render_template(
        "booksBS.html", 
        title="My Books !",
        books=get_sample())


@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = books[int(id)-1]
    return render_template(
        "detail.html",
        book=book)

class AuthorForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Nom', validators =[DataRequired()])