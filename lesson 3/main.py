from flask import Flask

import random

app = Flask(__name__)



@app.route("/")
def hello_world():
    facts = ['Я сигма', 'Меня зовут Бауыржан', 'Мне 18 лет']
    fact = random.choice(facts)
    return f'<h1>{fact}</h1>'

app.run(debug=True)