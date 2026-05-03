student=str(input("Enter your name:"))
age=int(input("Enter your age:"))
fav_subject=str(input("Enter your favourite subject:"))

Student_record = {
    "Name" : student,
    "student_age" : age,
    "favourite_subject" : fav_subject
}

print("\n","Student Record:")
print("Name:",Student_record["Name"])
print("Age:",Student_record["student_age"])
print("Favorite Subject:",Student_record["favourite_subject"])