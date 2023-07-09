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
print("\n -- Displaying Students Documents from find() Query")

# loop over student documents and output results
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " +doc["last_name"] + "\n")

# create new student document
luke = {
    "student_id": "1010",
    "first_name": "Luke",
    "last_name": "Skywalker"
}

# insert new student document into MongoDB Atlas
luke_student_id = students.insert_one(luke).inserted_id

# insert statements 
print("\n --Insert Statements  ")
print(" Inserted student records into the students collection with document_id " + str(luke_student_id))

# use find_one() method using student_id 1010
luke = students.find_one({"student_id": "1010"})

# show results
print("\n --Displaying Student DOC ")
print("  Student ID: " + luke_student_id["student_id"] + "\n First Name: " + luke_student_id["first_name"] + "\n Last Name: " + luke_student_id["last_name"] + "\n")

# use delete_one method to remove luke_student_id
deleted_luke_student_id = students.delete_one({"student_id": "1010"})

#display all students in collection
new_list = students.find({})

# display message for students documents
print("\n -- Displaying Students Documents from find() Query")

# loop over student documents and output results
for doc in new_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " +doc["last_name"] + "\n")

# end of program message
input("\n\n End of program, press any key to continue...")



