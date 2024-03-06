from flask import Flask, render_template

app = Flask(__name__)

test_name = "Python project"
max_score = 100
students = [
    {"name": "Jhon", "score": 100},
    {"name": "Victor", "score": 70},
    {"name": "Max", "score": 92},
    {"name": "Oleh", "score": 78}
]

@app.route('/results')
def result():
    context = {
        "title": "Results",
        "students": students,
        "test_name": test_name,
        "max_score": max_score
    }
    return render_template("results.html", **context)


@app.route('/')
def index():
    return render_template('base.html', title='Jinja_Test')


if __name__ == "__main__":
    app.run(debug=True)
