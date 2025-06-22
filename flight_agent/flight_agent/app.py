from flask import Flask, request, render_template, jsonify
from agent import agent

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/query", methods=["POST"])
def query():
    q = request.json.get("query")
    resp = agent.run(q)
    return jsonify({"response": resp})

if __name__ == "__main__":
    app.run(port=5000, debug=True)

