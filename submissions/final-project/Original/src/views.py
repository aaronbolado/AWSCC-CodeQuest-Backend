from flask import Blueprint, render_template, request, redirect, url_for
from .model import PasswordEntry
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    entries = PasswordEntry.query.all()
    return render_template("home.html", entries=entries)

@views.route("/add", methods=["POST"])
def add_entry():
    email = request.form.get('email')
    website = request.form.get('website')
    password = request.form.get('password')
    new_entry = PasswordEntry(website=website, email=email, password=password)
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('views.home'))

@views.route("/update/<id>", methods=["PATCH"])
def update_entry(id):
    
    # get data from form
    email = request.json.get('email')
    website = request.json.get('website')
    password = request.json.get('password')
    
    # updates
    entry = PasswordEntry.query.get(id)
    entry.email = email
    entry.website = website
    entry.password = password
    db.session.commit()
    return ({"result": "success"})

@views.route("/delete/<id>", methods=["DELETE"])
def delete_entry(id):
    entry = PasswordEntry.query.get(id)
    if entry:
        db.session.delete(entry)
        db.session.commit()
        return ({"results": "success"})
    return ({"results": "error"})
    