from app import app
from flask import render_template, request, flash

@app.route("/", methods=["GET", "POST"])
@app.route("/stocks")
def index():
    if request.method == "POST":
        flash(f"Sign up comppleted for {request.form.to_dict()['email']}.")
        with open('signups.txt', 'a') as f:
            f.write(f"\n{request.form.to_dict()['email']}")
    return render_template('index.html'), 200