from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import sqlite3

app = Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'smarodeen@gmail.com'      # Your email
app.config['MAIL_PASSWORD'] = "fvym xwrh vuwp ffmq"             # Your email password
app.config['MAIL_DEFAULT_SENDER'] = 'smarodeen@gmail.com'

mail = Mail(app)

def get_db_connection():
    conn = sqlite3.connect('/form_data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/submit', methods=['POST'])
def submit_form():
    print("Received request")
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Data received - Name: {name}, Email: {email}, Message: {message}")

        # Insert into the database
        conn = get_db_connection()
        conn.execute('INSERT INTO submissions (name, email, message) VALUES (?, ?, ?)',
                     (name, email, message))
        conn.commit()
        conn.close()

        # Send a success email
        if email: 
            msg = Message("Form Submission Successful", recipients=[email])
            msg.body = "Thank you for submitting the form! Your submission was successful."
            mail.send(msg)

        return jsonify({"status": "success", "message": "Form submitted successfully"}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500
