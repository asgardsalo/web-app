from flask import Flask, request, render_template, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your-secure-key'

# MySQL config
db_config = {
    'host': 'your-db-host',
    'user': 'your-db-user',
    'password': 'your-db-password',
    'database': 'fees'
}

user_db_config = {
    'host': 'your-db-host',
    'user': 'your-db-user',
    'password': 'your-db-password',
    'database': 'users'
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    uname = request.form['username']
    pwd = request.form['password']
    conn = mysql.connector.connect(**user_db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (uname, pwd))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        session['user'] = uname
        return redirect('/dashboard')
    else:
        return "Invalid credentials", 403

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        name = request.form['name']
        uname = request.form['username']
        pwd = request.form['password']
        conn = mysql.connector.connect(**user_db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, username, password) VALUES (%s, %s, %s)", (name, uname, pwd))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    surname = request.form['surname']
    grade = request.form['grade']
    fee = request.form['fee']
    paid = 1 if request.form.get('paid') else 0
    parent = request.form['parent']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO fees (name, surname, grade, fee, paid, parent) VALUES (%s, %s, %s, %s, %s, %s)",
                   (name, surname, grade, fee, paid, parent))
    conn.commit()
    cursor.close()
    conn.close()
    return "Saved!"