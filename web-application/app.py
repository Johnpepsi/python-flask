# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory users (you can replace this with a database in real applications)
users = {
    "user1": "password123",
    "user2": "securepassword"
}

@app.route('/', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate credentials
        if username in users and users[username] == password:
            return redirect(url_for('welcome', username=username))
        else:
            error = "Invalid username or password!"
            return render_template('index.html', error=error)
    
    return render_template('index.html')

@app.route('/welcome/<username>')
def welcome(username):
    return f"Welcome, {username}!"

if __name__ == '__main__':
    app.run(debug=True)

