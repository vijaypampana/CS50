from flask import Flask, render_template, request
import utilities

app = Flask(__name__)  # A new web application is a flask application, app is a variable which can be used in the below file ex @app.route


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/jsonBeautifier", methods=['GET', 'POST'])
def jsonBeautifier():
    if request.method == 'POST':
        rawJson = request.form.get("JSONDocumentTextBox", type=str)
        return render_template("jsonBeautifier.html", rawJson=utilities.jsonBeautifierprocess(rawJson))
    else:
        return render_template("jsonBeautifier.html")


@app.route('/xmlBeautifier', methods=['GET', 'POST'])
def xmlBeautifier():
    if request.method == 'POST':
        rawXml = request.form.get("XmlDocumentTextBox")
        return render_template("xmlBeautifier.html", rawXml=utilities.xmlBeautifierprocess(rawXml))
    else:
        return render_template("xmlBeautifier.html")


@app.route("/createUser", methods=['GET', 'POST'])
def createUser():
    if request.method == 'POST':
        env = request.form.get("env")
        version = request.form.get("version")
        apikey = request.form.get("apikey")
        clientCode = request.form.get("clientCode")
        return render_template("createNewUser.html", userCode=utilities.createNormalUser(env, version, apikey, clientCode))
    else:
        return render_template("createNewUser.html")


@app.route("/limitValidator", methods=['GET', 'POST'])
def limitValidator():
    return "This is a limit validator Page"


if __name__ == "__main__":
    app.run()
