import json

DATABASE_FILE = "database.json"

def load_data():
    try:
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_data(data):
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)


def create_student(name, age, favorite_subject, favorite_color, favorite_song):
    data = load_data()

    student = {
        "name": name,
        "age": age,
        "favorite_subject": favorite_subject,
        "favorite_color": favorite_color,
        "favorite_song": favorite_song
    }

    data.append(student)
    save_data(data)

    print(f"{name} added successfully.")


def read_students():
    data = load_data()

    print("Student Database:\n")

    for student in data:
        print(student)


def update_school(campus_name):
    data = load_data()

    for student in data:
        student["school"] = campus_name

    save_data(data)

    print("All students updated with school field.")


def delete_by_color():
    data = load_data()

    colors_to_delete = ["red", "blue", "yellow"]

    new_data = [student for student in data if student["favorite_color"].lower() not in colors_to_delete]

    save_data(new_data)

    print("Students with favorite color red, blue, or yellow deleted.")


create_student("RJ UJAN", 13, "Math 2", "yellow", "pag ibig")
create_student("Zoe Calumpang", 13, "Physics", "red", "Konsensiya")
create_student("Kiara Dongon", 14, "physics", "Purple", "Aura")
create_student("Charina Marco", 13, "Math 2", "blue", "yakap")
create_student("Cassandra Marie", 13, "Biology", "blue", "Emily's Song")


read_students()

update_school("PSHS CVISCC") 
read_students()

delete_by_color()

read_students()