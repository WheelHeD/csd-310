from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.7g9uqqb.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

john = {
    "student_id": "1007",
    "first_name": "John",
    "last_name": "Johnson",
    "enrollments": [
        {
            "term": "Summer 2023",
            "gpa": "3.5",
            "start_date": "May 5, 2023",
            "end_date": "August 5, 2023",
            "courses": [
                {
                    "course_id": "CYBR101",
                    "description": "Intro to Cybersecurity",
                    "instructor": "James Dean",
                    "grade": "B+"
                },
                {
                    "course_id": "CYBR102",
                    "description": "Network Security",
                    "instructor": "Bob Dole",
                    "grade": "B"
                }
            ]
        }
    ]
}

sarah = {
    "student_id": "1008",
    "first_name": "Sarah",
    "last_name": "Conner",
    "enrollments": [
        {
            "term": "Summer 2023",
            "gpa": "3.75",
            "start_date": "May 5, 2023",
            "end_date": "August 5, 2023",
            "courses": [
                {
                    "course_id": "CYBR101",
                    "description": "Intro to Cybersecurity",
                    "instructor": "James Dean",
                    "grade": "A"
                },
                {
                    "course_id": "CYBR102",
                    "description": "Network Security",
                    "instructor": "Bob Dole",
                    "grade": "B"
                }
            ]
        }
    ]
}
MongoDB: insert_one()
peter = {
    "student_id": "1009",
    "first_name": "Peter",
    "last_name": "Parker",
    "enrollments": [
        {
            "term": "Summer 2023",
            "gpa": "4.0",
            "start_date": "May 5, 2023",
            "end_date": "August 5, 2023",
            "courses": [
                {
                    "course_id": "CYBR101",
                    "description": "Intro to Cybersecurity",
                    "instructor": "James Dean",
                    "grade": "A+"
                },
                {
                    "course_id": "CYBR102",
                    "description": "Network Security",
                    "instructor": "Bob Dole",
                    "grade": "A+"
                }
            ]
        }
    ]
}

students= db.students

print("\n  INSERT STATEMENTS")
john_student_id= students.insert_one(john).inserted_id
print("  Inserted student record John Johnson into the students collection with document_id " + str(john_student_id))

sarah_student_id= students.insert_one(sarah).inserted_id
print("  Inserted student record Sarah Conner into the students collection with document_id " + str(sarah_student_id))

peter_student_id= students.insert_one(peter).inserted_id
print("  Inserted student record Peter Parker into the students collection with document_id ") +str(peter_student_id)
