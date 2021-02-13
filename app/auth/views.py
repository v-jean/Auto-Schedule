from flask import render_template, redirect, url_for, flash, request
from . import auth_bp
from ..models import User
from flask_login import login_user, login_required , logout_user
from .. import db

@auth_bp.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            return redirect(request.args.get("next") or url_for('main.home'))
        flash("Email o contraseña incorrectos.")
        return redirect(url_for('auth.login'))
    elif request.method == "GET":
        return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Haz cerrado sesión")
    return redirect(url_for("main.home"))

def validate_email(e):
    if User.query.filter_by(email=e).first():
        return False
    return True

def validate_username(u):
    if User.query.filter_by(username=u).first():
        return False
    return True

@auth_bp.route('/signup', methods=["POST","GET"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        if validate_email(email) and validate_username(username):
            user = User(email=email,
                        username=username,
                        password=password)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(request.args.get("next") or url_for('main.home'))
        elif not validate_email(email):
            flash("Ya existe una cuenta con este email")
            return redirect(url_for('auth.signup'))
        elif not validate_username(username):
            flash("Ya existe una cuenta con este nombre de usuario")
            return redirect(url_for('auth.signup'))    
    elif request.method == "GET":
        return render_template('auth/signup.html')