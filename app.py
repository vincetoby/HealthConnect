# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # Handle user registration logic
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    # Validate input and create new user account
    # Return JSON response
    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    # Handle user login logic
    username = request.form.get('username')
    password = request.form.get('password')
    # Authenticate user
    # Return JSON response
    return jsonify({'message': 'User logged in successfully'})

if __name__ == '__main__':
    app.run(debug=True)
  
