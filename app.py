# app.py – Flask backend setup
from flask import Flask, render_template, request

app = Flask(__name__)

# Route definitions for each page
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/solutions")
def solutions():
    return render_template("solutions.html")

@app.route("/impact")
def impact():
    return render_template("impact.html")

@app.route("/careers")
def careers():
    return render_template("careers.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Process form data here (e.g., send email or save subscription)
        name = request.form.get("name")
        email = request.form.get("email")
        # For now, just pass or send a thank-you response
        # In production, integrate email service or database
        pass
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

