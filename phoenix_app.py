from flask import Flask, render_template, request, redirect
import sys
import logging

# import SQLAlchemy

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route("/webdev")
def webdev():
    return render_template("webdev.html")

@app.route("/datascience")
def data():
    return render_template("datascience.html")

@app.route("/cybersecurity")
def cyber():
    return render_template("cyber.html")

@app.route("/testing")
def testing():
    return render_template("testing.html")

@app.route("/aboutus")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)