from flask import Flask, request, render_template, jsonify
from chatbot import get_answer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    response = get_answer(question)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
