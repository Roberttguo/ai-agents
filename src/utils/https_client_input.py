from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML form
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the submitted form
    user_input = request.form['user_input']
    return user_input
