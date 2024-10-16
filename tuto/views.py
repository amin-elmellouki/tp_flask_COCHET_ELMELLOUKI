from flask import url_for, redirect, render_template, flash
from .app import app, db
from .models import Author, get_author, get_sample, User
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField
from wtforms.validators import DataRequired
from hashlib import sha256
from flask_login import login_user, current_user, logout_user, login_required
from flask import request

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
   
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    next = HiddenField()
    
    def get_authenticated_user(self):
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            m = sha256()
            m.update(self.password.data.encode())
            hashed_password = m.hexdigest()
            if hashed_password == user.password:
                return user
        return None

@app.route("/login/", methods=["GET", "POST"])
def login():
    f = LoginForm()

    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            next_page = f.next.data or url_for("home")
            return redirect(next_page)
    
    return render_template("login.html", form=f)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/authors")
@login_required # Pour que cette page ne soit dispo que pour les users
def list_authors():
    authors = Author.query.all()  
    return render_template("list_author.html", authors=authors)
