from flask import Flask

app = Flask(__name__)

@app.route("/fizzbuzz")
def fizzbuzz():
    numbers = range(1, 101)
    return render_template('fizzbuzz.html', numbers=numbers)