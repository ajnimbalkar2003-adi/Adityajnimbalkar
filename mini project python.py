student = {}

while True:
    print("\n---- Student Management System ----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Student Result")
    print("4. Student Rank")
    print("5. Check Attendance")
    print("6. Show Student Details")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        try:
            rollNo = int(input("Enter Roll Number: "))
            marks = float(input("Enter Marks: "))
            attendance = float(input("Enter Attendance: "))

            student[name] = {
                "roll": rollNo,
                "marks": marks,
                "attendance": attendance
            }

        except:
            print("Enter valid numeric values")

    elif choice == "2":
        if not student:
            print("No students found")
        else:
            for name, data in student.items():
                print(name, ":", data)

    elif choice == "3":
        name = input("Enter Name: ")
        if name in student:
            marks = student[name]["marks"]
            if marks >= 40:
                print("Pass")
            else:
                print("Fail")
        else:
            print("Student not found")

    elif choice == "4":
        if not student:
            print("No students found")
        else:
            sorted_students = sorted(student.items(), key=lambda x: x[1]["marks"], reverse=True)

            print("\n--- RANK LIST ---")
            rank = 1
            for name, data in sorted_students:
                print(f"Rank {rank}: {name} - {data['marks']}")
                rank += 1

    elif choice == "5":
        if not student:
            print("No students found")
        else:
            for name, data in student.items():
                print(name, ":", data["attendance"])

    elif choice == "6":
        name = input("Enter Name: ")
        if name in student:
            print(student[name])
        else:
            print("Student not found")

    elif choice == "7":
        print("Program Closed")
        break

    else:
        print("Invalid choice")
