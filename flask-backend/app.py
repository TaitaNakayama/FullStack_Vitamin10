from flask import Flask, jsonify, request
import random

app = Flask(__name__)

quotes = [
    {"id": 1, "text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"id": 2, "text": "Code is like humor. When you have to explain it, it's bad.", "author": "Cory House"},
    {"id": 3, "text": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
    {"id": 4, "text": "Simplicity is the soul of efficiency.", "author": "Austin Freeman"},
    {"id": 5, "text": "Fix the cause, not the symptom.", "author": "Steve Maguire"},
]

next_id = 6


@app.route("/api/quote", methods=["GET"])
def get_random_quote():
    return jsonify(random.choice(quotes))


@app.route("/api/quotes", methods=["GET"])
def get_all_quotes():
    return jsonify(quotes)


@app.route("/api/quotes", methods=["POST"])
def create_quote():
    global next_id
    data = request.json or {}
    new_quote = {
        "id": next_id,
        "text": data.get("text", ""),
        "author": data.get("author", ""),
    }
    quotes.append(new_quote)
    next_id += 1
    return jsonify(new_quote), 201


@app.route("/api/quotes/<int:id>", methods=["PUT"])
def update_quote(id):
    data = request.json or {}
    for q in quotes:
        if q["id"] == id:
            if "text" in data:
                q["text"] = data["text"]
            if "author" in data:
                q["author"] = data["author"]
            return jsonify(q)
    return jsonify({"error": "Quote not found"}), 404


@app.route("/api/quotes/<int:id>", methods=["DELETE"])
def delete_quote(id):
    for i, q in enumerate(quotes):
        if q["id"] == id:
            quotes.pop(i)
            return jsonify({"message": f"Quote {id} deleted"})
    return jsonify({"error": "Quote not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
