from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from lxml import etree
import json

app = Flask(__name__)   #A new web application is a flask application, app is a variable which can be used in the below file ex @app.route

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jsonBeautifier")
def jsonBeautifier():
    return render_template("jsonBeautifier.html")

@app.route('/xmlBeautifier')
def xmlBeautifier():
    return render_template("xmlBeautifier.html")

@app.route("/createUser")
def createUser():
    return "Welcome to Create Automated User Page"

@app.route('/xmlBeautify', methods=["POST"])
def xmlBeautify():
    rawXml = request.form.get("XmlDocumentTextBox")
    return render_template("xmlBeautifier.html", rawXml=str.replace((BeautifulSoup(rawXml, "lxml").prettify(encoding='UTF-8')).decode("UTF-8"), "\n", "\r\n"))
    # return etree.tostring(etree.parse(rawXml), pretty_print=True, xml_declaration=True, encoding='UTF-8')


if __name__ == "__main__":
    app.run()