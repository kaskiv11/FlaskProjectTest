from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def add_user(conn, user):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (user.username, user.password))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def get_user(conn, username):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        if row:
            return User(row[0], row[1], row[2])
    except sqlite3.Error as e:
        print(e)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = create_connection('database.db')
        if conn is not None:
            create_table(conn)
            existing_user = get_user(conn, username)
            if existing_user:
                flash('Користувач з таким ім\'ям вже існує', 'error')
                return redirect(url_for('register'))

            hashed_password = generate_password_hash(password)
            new_user = User(None, username, hashed_password)
            add_user(conn, new_user)

            flash('Ви успішно зареєструвалися!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Помилка підключення до бази даних', 'error')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = create_connection('database.db')
        if conn is not None:
            user = get_user(conn, username)
            if user and check_password_hash(user.password, password):
                session['username'] = username
                flash('Ви успішно увійшли!', 'success')
                return redirect(url_for('profile'))
            else:
                flash('Невірне ім\'я користувача або пароль. Будь ласка, спробуйте ще раз.', 'error')
        else:
            flash('Помилка підключення до бази даних', 'error')

    return render_template('login.html')


@app.route('/')
def index():
    return render_template('index.html')


from flask import session


@app.route('/logout')
def logout():
    # Clear user session
    session.pop('username', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('index'))


from flask import render_template, session


@app.route('/profile')
def profile():

    username = session.get('username')

    return render_template('welcome.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
