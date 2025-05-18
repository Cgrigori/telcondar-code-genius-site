# -*- coding: utf-8 -*-
"""
Created on Thu May  8 09:54:52 2025

@author: grigo
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True)