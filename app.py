from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Defining the home page of our site
@app.route("/index")  
def index():
	return render_template("index.html")


@app.route("/classes")
def classes():
    return render_template("classes.html")

@app.route("/instructors")
def instructors():
    return render_template("instructors.html")

if __name__ == "__main__":
    app.run()
