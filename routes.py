from flask import current_app as app
from flask import redirect, url_for, render_template, request
from flask_login import current_user, login_required
from flask_login import login_user, logout_user
from app import login_manager, rooms
from models import db, User
from forms import *


@app.route('/')
@login_required
def home():
    return render_template('chat.html', user=current_user.username, rooms=rooms)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        valid = validate_login(request.form)
        if valid:
            login_user(valid)
            return redirect(url_for('home'))
        return render_template('login.html', form=LoginForm(None))
    return render_template('login.html', form=LoginForm(None))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        added = add_user(request.form)
        if added:
            login_user(added)
            return redirect(url_for('home'))
        return render_template('signup.html', form=SignupForm(None))
    return render_template('signup.html', form=SignupForm(None))

def validate_login(form):
    username = form.get('username')
    password = form.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password=password):
        return user
    return False

def add_user(form):
    username = form.get('username')
    password = form.get('password')
    user = User.query.filter_by(username=username).first()
    if user:
        return False
    try:
        user = User(username=username)
        user.set_password(password=password)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(e)
        return False
    return user

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    #flash('You must be logged in to view that page.')
    return redirect(url_for('login'))
