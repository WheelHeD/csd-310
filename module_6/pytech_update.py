# statement to import MongoClient
from pymongo import MongoClient

# connection string from MongoDB Atlas
url = "mongodb+srv://admin:admin@cluster0.7g9uqqb.mongodb.net/?retryWrites=true&w=majority"

# call the MongoClient and pass-in url variable to connect to cluster
client = MongoClient(url)

# variable to connect to pytech database
db = client.pytech

# variable used to access students collection
students = db.students

# search for all students in students collection
student_list = students.find({})

# display message for students documents
print("\n -- Displaying Students Documents from find() query")

# loop over student documents and output results
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " +doc["last_name"] + "\n")

# update student #1007 
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Johnson IV"}})

# find updated student #1007
john = students.find_one({"student_id": "1007"})

# display message for student #1007
print("\n Displaying Student Document 1007")

# output updated student document
print(" Student ID: " + john["student_id"] + "\n First Name: " + john["first_name"] + "\n Last Name: " + john["last_name"] + "\n")

# end of program message
input("\n\n End of program, press any key to continue...")






