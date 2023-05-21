from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# Start server
app = Flask(__name__)
FlaskJSON(app)


# Connect to MongoDB cluster
uri = "mongodb+srv://NithinSenthil:BOMBOCLAAT@aggiereuseinventory.mesyrt5.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))


# Server/Database connection testing
@app.route("/testConnection")
def testConnection():
    try:
        client.admin.command('ping')
        ping = "Pinged your deployment. You successfully connected to MongoDB!\n"
    except Exception as e:
        print(e)

    return ping


# Push to cluster
@app.route('/submit', methods=['POST'])
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
