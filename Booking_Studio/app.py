from flask import Flask, flash, render_template, request, redirect, session
from flask_bcrypt import Bcrypt  # Import Bcrypt for password hashing
from mysqlConnect import db  # Assuming db is defined in mysqlconnect.py

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = '002219'  # Set a secret key

@app.route('/')
def home():
    return render_template('front-page.html')

@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form['email']
        password = request.form['password']
        fornavn = request.form['fornavn']
        efternavn = request.form['efternavn']
        telefonnr = request.form['telefonnr']

        # Form validation
        if not (email and password and fornavn and efternavn and telefonnr):
            error = 'Please fill in all the fields'
            return render_template('registration.html', error=error)

        # Create a cursor to interact with the database
        cur = db.cursor()

        # Check if the email already exists
        result = cur.execute("SELECT * FROM bruger WHERE email = %s", (email,))
        result = cur.fetchone()

        if result:
            error = 'Email already exists'
            return render_template('registration.html', error=error)

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Insert the new user into the database with the hashed password
        cur.execute("INSERT INTO bruger (email, password, fornavn, efternavn, telefonnr) VALUES (%s, %s, %s, %s, %s)",
                    (email, hashed_password, fornavn, efternavn, telefonnr))
        db.commit()

        # Close the cursor
        cur.close()

        # Redirect to the login page
        return redirect('/login')

    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = db.cursor(dictionary=True)  
        cur.execute("SELECT * FROM bruger WHERE email = %s", (email,)) 
        all_users = cur.fetchall()

        for bruger in all_users:
            if bcrypt.check_password_hash(bruger['password'], password):
                # Password is correct, set up the session
                session['bruger_id'] = bruger['bruger_id'] 
                session['email'] = bruger['email'] 
                flash('Login successful', 'success')
                return redirect('/booking')

        flash('Login failed. Check your email and password.', 'danger')

    return render_template('login.html')


@app.route('/booking', methods=['POST'])
def booking():
    return render_template('booking.html')

@app.route('/confirm', methods=['POST'])
def confirm_booking():
    return render_template('confirm.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
