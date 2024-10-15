from flask import url_for, redirect, render_template, flash
from .app import app, db
from .models import Author, get_author, get_sample
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired


class AuthorForm(FlaskForm):
    id = HiddenField('id') 
    name = StringField('Nom', validators=[DataRequired()])

@app.route("/")
def home():
    return render_template(
        "booksBS.html",
        title="My Books !",
        books=get_sample()
    )

@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = books[int(id)-1]
    return render_template("detail.html", book=book)

@app.route("/add/author", methods=["GET", "POST"])
def add_author():
    form = AuthorForm()

    if form.validate_on_submit():
        new_author = Author(name=form.name.data)
        db.session.add(new_author)
        db.session.commit()

        flash(f"Auteur '{new_author.name}' ajouté avec succès!", 'success')
        return redirect(url_for('one_author', id=new_author.id))

    return render_template("add-author.html", form=form)

@app.route("/edit/author/<int:id>")
def edit_author(id):
    a = get_author(id)
    if not a:
        return "Author not found", 404

    form = AuthorForm(id=a.id, name=a.name)
    return render_template(
        "edit-author.html",
        author=a, form=form
    )

@app.route("/save/author", methods=["POST"])
def save_author():
    form = AuthorForm()

    if form.validate_on_submit():
        if form.id.data:
            author = get_author(int(form.id.data))
            author.name = form.name.data
        else:
            author = Author(name=form.name.data)
            db.session.add(author)

        db.session.commit()
        flash(f"Auteur '{author.name}' enregistré avec succès!", 'success')
        return redirect(url_for('one_author', id=author.id))

    return render_template("add-author.html", form=form)

@app.route("/one_author/<int:id>")
def one_author(id):
    a = get_author(id)
    if not a:
        return "Author not found", 404
    return render_template(
        "detail_author.html",
        author=a
    )
