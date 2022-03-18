from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Defining the home page of our site
@app.route("/index.html")  # this sets the route to this page
def home():
	return render_template("/index")

@app.route("/instructors.html")
def instructors():
    return render_template("instructors.html")

@app.route("/classes.html")
def classes():
    return render_template("classes.html")

@app.route("/pricing.html")
def pricing():
    return render_template("pricing.html")

if __name__ == "__main__":
    app.run()
