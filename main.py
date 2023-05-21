from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_cors import CORS, cross_origin


app = Flask(__name__)
FlaskJSON(app)
CORS(app)

@app.route("/api/testConnection")
def testConnection():
    rv = "<p>Server connection works</p>"
    return json_response(200)



@app.route('/api/submit', methods=['POST'])
def submit():
    # We use 'force' to skip mimetype checking to have shorter curl command.
    data = request.get_json(force=True)
    try:
        numShirts = int(data['shirts'])
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')

    print("There are " + str(numShirts) + " shirts.")

    return json_response(200, status="Upload Confirmed")


@app.route('/generateAnalysis')
def generateAnalysis():
    return "Analysis generated\n"

app.run(port=8000, debug=True)