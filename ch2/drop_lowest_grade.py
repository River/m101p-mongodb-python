import pymongo

connection = pymongo.MongoClient('localhost', 27017)
db = connection.students

grades = db.grades.find().sort([("student_id", pymongo.ASCENDING), ("score", pymongo.ASCENDING)])

current_student = -1
for grade in grades:
    if grade['student_id'] > current_student:
        db.grades.remove({'_id': grade['_id']})
        current_student += 1
