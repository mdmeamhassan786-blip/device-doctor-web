from flask import Flask, render_template, request, jsonify
from doctor import diagnose

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/diagnose", methods=["POST"])
def api_diagnose():
    problem_text = request.form.get("problem", "")
    solution = diagnose(problem_text)
    return jsonify({"solution": solution})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
