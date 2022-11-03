from flask import Blueprint, render_template, request, flash, url_for, redirect
from .models import User
from website import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login Successful', category='success')
                login_user(user, remember=True)
            else:
                flash("Incorrect Password", category='error')
        else:
            flash("User Email Doesn't Exist", category='error')

        return redirect(url_for('auth.user_home'))

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login', user=current_user))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        surname = request.form.get('surname')
        username = request.form.get('username')
        fav_team = request.form.get('fav_tea,')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("User Email Exists")
        elif password1 != password2:
            flash("Passwords Do Not Match", category='error')
        elif len(password1) < 7:
            flash("Password Must Be At Lease 7 Characters", category='error')
        elif fav_team == "Select Team":
            flash("Please Choose Favourite Team", category='error')
        else:
            new_user = User(first_name=first_name, surname=surname, username=username, fav_team=fav_team, email=email, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Registration Complete!", category='success')
            return redirect(url_for('auth.user_home', user=current_user))
    return render_template('signup.html', user=current_user)

@auth.route('/user_home')
@login_required
def user_home():
    return render_template('user_home.html', user=current_user)