from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Handle form submission logic here
    print(f"Name: {name}, Email: {email}, Message: {message}")
    return 'Form submission successful!'

if __name__ == '__main__':
    app.run(debug=True)
