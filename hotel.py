print("Welcome to Green Valley School")

students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student class: ")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully")

def display_students():
    if len(students) == 0:
        print("No students found")
    else:
        for student in students:
            print("----------------")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Class:", student["grade"])

def search_student():
    name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student Found")
            print(student)
            found = True
            break

    if found == False:
        print("Student not found")

def delete_student():
    name = input("Enter student name to delete: ")

    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Student deleted")
        else:
            print("Student not found")

def main():
    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Program closed")
            break

        else:
            print("Invalid choice")

main()