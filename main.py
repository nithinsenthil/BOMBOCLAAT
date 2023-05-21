from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_cors import CORS, cross_origin


# Start server
app = Flask(__name__)
FlaskJSON(app)
CORS(app)


# Connect to MongoDB cluster
uri = "mongodb+srv://NithinSenthil:BOMBOCLAAT@aggiereuseinventory.mesyrt5.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))


# Server/Database connection testing
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


# Pull data for analysis
@app.route('/generateAnalysis')
def generateAnalysis():

    return "Feature Currently Unavailable\n"

app.run(port=8000, debug=True)

