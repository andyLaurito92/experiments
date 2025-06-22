from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint # to print nested data
import os

user = os.environ["user"]
password = os.environ["password"]
cluster = os.environ["cluster"]

uri = f"mongodb+srv://{user}:{password}@{cluster}/?retryWrites=true&w=majority&appName=andy-testing"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


for db_info in client.list_database_names():
   print(db_info)



print("========== Sample MFLIX ==========")

db = client['sample_mflix']

# List all the collections in 'sample_mflix':

collections = db.list_collection_names()

for collection in collections:
   print(collection)


def show_all_documents(collection_name):
    collection = db[collection_name]
    # To list all documents in a collection
    cursor = collection.find({})
    for document in cursor:
        pprint(document)

# show_all_documents('users')

print("Emails starting w/a")
emails_startw_a = db['users'].find({"email": {"$regex": "^a"}})
for emails_with_a in emails_startw_a:
    pprint(emails_with_a)
