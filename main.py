from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(__name__)
FlaskJSON(app)


@app.route("/testConnection")
def testConnection():
    return "<p>Server connection works</p>"


@app.route('/submit', methods=['POST'])
def submit():
    # We use 'force' to skip mimetype checking to have shorter curl command.
    data = request.get_json(force=True)
    try:
        numShirts = int(data['shirts'])
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')

    print("There are " + str(numShirts) + " shirts.")

    return json_response(400, status="Upload Confirmed")


@app.route('/generateAnalysis')
def generateAnalysis():
    return "Analysis generated\n"