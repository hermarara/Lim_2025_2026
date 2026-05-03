
students=[]

for i in range (3):
    Student_dict = {}

    Student_dict["name"] = input("Enter name:")
    Student_dict["age"] = input("Enter age:")
    Student_dict["grade"] = input("Enter grade:")
    students.append(Student_dict)

for i in students:
    print ("\nClass Directory")
    print ("Name:", i["name"])
    print ("Age:", i["age"])
    print ("Grade:", i["grade"])


