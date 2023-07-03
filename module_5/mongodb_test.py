
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.7g9uqqb.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print(db.list_collection_names)

input("\n  End of program, press any key to exit...")