import random
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

QUOTES = [
    {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"quote": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
    {"quote": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"quote": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein"},
    {"quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
    {"quote": "Whether you think you can or you think you can't, you're right.", "author": "Henry Ford"},
    {"quote": "The best time to plant a tree was 20 years ago. The second best time is now.", "author": "Chinese Proverb"},
    {"quote": "Do not watch the clock. Do what it does. Keep going.", "author": "Sam Levenson"},
    {"quote": "It always seems impossible until it's done.", "author": "Nelson Mandela"},
    {"quote": "Stay hungry, stay foolish.", "author": "Stewart Brand"},
]


@app.route("/")
def home():
    q = random.choice(QUOTES)
    return f"<h1>Quote of the Day</h1><p>\"{q['quote']}\"</p><p>— {q['author']}</p>"


@app.route("/api/quote")
def get_quote():
    return jsonify(random.choice(QUOTES))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
