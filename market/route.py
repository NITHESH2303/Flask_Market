from market import app
from flask import render_template
from market.models import item
from market.forms import RegisterForm


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = item.query.all()
    return render_template('market.html', items=items)


@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)
