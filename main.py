from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_cors import CORS, cross_origin
from datetime import date, time
import bson

# Start server
app = Flask(__name__)
FlaskJSON(app)
CORS(app)


# Connect to MongoDB cluster
uri = "mongodb+srv://NithinSenthil:BOMBOCLAAT@aggiereuseinventory.mesyrt5.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
logs = client["Logs"]
masterCol = (client["Master"])["MasterLog"]


# Server/Database connection testing
@app.route("/api/testConnection")
def testConnection():
    # rv = "<p>Server connection works</p>"

    rv = None
    oldMasterLog = (masterCol.find())
    for doc in oldMasterLog:
        rv = doc
        break

    for i in rv:
        print(rv[i])

    # for i in logDict:
    #     print(logDict[i])

    return json_response(200)


@app.route("/api/submit/", methods=["POST"])
def submit():
    # We use 'force' to skip mimetype checking to have shorter curl command.
    data = request.get_json(force=True)
    try:
        numShirt = int(data['shirt'])
        numTanktop = int(data['tankTop'])
        numLongSleeve = int(data['longSleeve'])
        numJacket = int(data['jacket'])
        numPants = int(data['pants'])
        numJeans = int(data['jeans'])
        numShorts = int(data['shorts'])
        numSkirt = int(data['skirt'])
        totalIn = int(data['totalIn'])
        totalOut = int(data['totalOut'])

    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')

    dayLog = logs[str(date.today())]

    tempLog = {
        "shirt": numShirt,
        "tankTop": numTanktop,
        "longSleeve": numLongSleeve,
        "jacket": numJacket,
        "pants": numPants,
        "jeans": numJeans,
        "shorts": numShorts,
        "skirt": numSkirt,
        "totalIn": totalIn,
        "totalOut": totalOut
    }

    oldMasterLog = (masterCol.find())
    for doc in oldMasterLog:
        rv = doc


    masterTempLog = {
        "shirt": numShirt + rv["shirt"],
        "tankTop": numTanktop + rv["tankTop"],
        "longSleeve": numLongSleeve + rv["longSleeve"],
        "jacket": numJacket + rv["jacket"],
        "pants": numPants + rv["pants"],
        "jeans": numJeans + rv["jeans"],
        "shorts": numShorts + rv["shorts"],
        "skirt": numSkirt + rv["skirt"],
        "totalIn": totalIn + rv["totalIn"],
        "totalOut": totalOut + rv["totalOut"]
    }

    status1 = dayLog.insert_one(tempLog)
    status2 = masterCol.insert_one(masterTempLog)

    if status1 and status2:
        return json_response(200, status="Upload Confirmed")
    return json_response(200, status="Error could not update database")


# Pull data for analysis
@app.route('/generateAnalysis')
def generateAnalysis():

    return "Coming soon to stores near you!\n"

app.run(port=8000, debug=True)

