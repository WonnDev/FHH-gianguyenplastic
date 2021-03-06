

from appdb import app
from flask import render_template




@app.route("/")
def home():
	
    return render_template('index.html')


@app.route('/product')
def product():

    return render_template('products/product.html')

@app.route('/contact')
def contact():
    return render_template('home/news/contact.html')

@app.route('/introduce')
def introduce():
    return render_template('home/news/introduce.html')

@app.route('/new')
def new():
    return render_template('home/news/news.html')

@app.route('/header')
def header():
    return render_template('home/news/header-t.html')