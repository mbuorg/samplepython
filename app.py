import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

def get_db_connection():
    conn = sqlite3.connect('database.db', timeout=20)
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.config['SECRET_KEY'] = 'samplekey'

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM hospital').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
         name = request.form['name']
         address = request.form['address']
         contact = request.form['contact']
         conn = get_db_connection()
         conn.execute('INSERT INTO hospital (name, address, phone) VALUES (?, ?, ?)', (name, address, contact))
         conn.commit()
         conn.close()
         return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/about')
def about():
    return render_template('about.html')
