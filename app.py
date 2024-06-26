from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['devops_students']

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration form submission
        # Example: Save data to MongoDB
        users = db.users
        user_data = {
            'first_name': request.form['first'],
            'last_name': request.form['last'],
            'email': request.form['email'],
            'password': request.form['password'],
            'mobile': request.form['mobile'],
            'gender': request.form['gender']
        }
        users.insert_one(user_data)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
