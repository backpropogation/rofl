from flask import render_template, url_for, flash, redirect
from someprop import app, db, bcrypt
from someprop.forms import RegistrationForm, LoginForm
from someprop.models import User, Post, RentProperty
from _datetime import datetime


class Controller:
    @staticmethod
    @app.route("/")
    @app.route("/home")
    def home():
        posts = RentProperty.query.all()
        return render_template('home.html', posts=posts)

    @staticmethod
    @app.route("/about")
    def about():
        return render_template('about.html', title='About')

    @staticmethod
    @app.route("/register", methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            #TO REFACTOR USING ABSTRACT FAB
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash(f'Your account has been created! You are now able to log in!', 'success')
            return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)

    @staticmethod
    @app.route("/login", methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            if form.email.data == 'b@mail.com' and form.password.data == '12345678':
                flash('You have been logged in!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
        return render_template('login.html', title='Login', form=form)

    @staticmethod
    @app.route("/report", methods=['GET'])
    def report():
        return render_template('home.html')
