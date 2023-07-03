from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.7g9uqqb.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students= db.students

student_list= students.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("  Student ID: " +doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n") 


    peter = students.find_one({"student_id: 1009"})


                               