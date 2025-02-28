from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Load Questions from JSON file
def load_questions():
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            return json.load(file)
    return {}

# Home Route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        session["name"] = request.form["name"]
        session["age"] = request.form["age"]
        session["nationality"] = request.form["nationality"]
        session["visa_type"] = request.form["visa_type"]
        return redirect(url_for("interview"))

    return render_template("index.html")

# Interview Route
@app.route("/interview", methods=["GET", "POST"])
def interview():
    questions = load_questions().get(session.get("visa_type"), [])

    if request.method == "POST":
        responses = {q: request.form.get(q, "") for q in questions}
        session["responses"] = responses
        return redirect(url_for("results"))

    return render_template("interview.html", questions=questions)

# Results Route
@app.route("/results")
def results():
    responses = session.get("responses", {})
    return render_template("results.html", responses=responses)

if __name__ == "__main__":
    app.run(debug=True)
