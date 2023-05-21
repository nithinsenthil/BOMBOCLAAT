from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://NithinSenthil:BOMBOCLAAT@aggiereuseinventory.mesyrt5.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    db = client["sample_airbnb"]
    mycol = db.list_collection_names()
    print(mycol)

except Exception as e:
    print(e)


# import urllib3
# import json
#
# url = "https://us-west-2.aws.data.mongodb-api.com/app/data-candv/endpoint/data/v1/action/findOne"
# http = urllib3.PoolManager()
#
# payload = json.dumps({
#     "collection": "<COLLECTION_NAME>",
#     "database": "<DATABASE_NAME>",
#     "dataSource": "AggieReuseInventory",
#     "projection": {
#         "_id": 1
#     }
# })
# headers = {
#   'Content-Type': 'application/json',
#   'Access-Control-Request-Headers': '*',
#   'api-key': "BPlH6NUFAN4oL5P8pMNX4hNwT3tLWLxJU73tgtElPLv4U0gz7vg0pM0KjkxU0StQ",
# }
#
# # response = requests.request("POST", url, headers=headers, data=payload)
# resp = http.request("POST", url, headers=headers, body=payload)
#
# print(resp.status)
# print(resp.data)
#
# # print(response.text)
