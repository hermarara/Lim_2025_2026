students = []

for i in range(3):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)

for student in students:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Grade:", student["grade"])
    print("---")
