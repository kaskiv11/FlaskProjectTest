from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/login')
def index_login():
    return render_template('login.html')


max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Yaroslav", "score": 100},
    {"name": "Egor", "score": 59},
    {"name": "Nikita", "score": 93},
    {"name": "Illia", "score": 78},
    {"name": 'Kyrylo', "score": 99},
    {"name": "Alex", "score": 11},
    {"name": "Mia", "score": 82},
    {"name": "Polina", "score": 69}
]


@app.route("/")
def index():
    return render_template('base.html', title='All Work')


@app.route("/results/")
def results():
    context = {
        'title': 'Results',
        'students': students,
        'test_name': test_name,
        'max_score': max_score
    }
    return render_template('results.html', **context)


@app.route('/process_login', methods=['POST'])
def process_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Тут ви можете додати логіку для перевірки введених даних

        return render_template('welcome.html', username=username, password=password)



if __name__ == '__main__':
    app.run(debug=True)
