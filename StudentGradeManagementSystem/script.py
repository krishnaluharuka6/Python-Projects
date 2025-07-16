student_grades = {}

print("___Welcome to Student Grade Management System___")

def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with grade = {grade} \n")

def update_student(name, grade):
    if name in student_grades:
            student_grades[name] = grade
            print(f"{name}'s total grade is updated to {grade} \n")
    else:
        print("This student is not found")
    
def view_student_details():
    if student_grades:
        print(f"The student details are: ")
        for name,grade in student_grades.items():
            print(f"{name} : {grade}")
        # print("\n")
    else:
        print("No data found \n")

            

def del_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name}'s details is deleted \n")
    else:
        print("This student not found \n")



def main():
    while True:
        print("""Enter
1 to add student grades
2 to update
3 to view
4 to delete
5 to exit from the System \n """)
        operation = int(input())

        if operation == 1:
            name = input("Enter name of the student: ").title()
            grade = int(input("Enter grade of the student "))
            add_student(name, grade)
            

        elif operation == 2:
            name = input("Enter student name to update: ").title()
            grade = input("Enter updated grade ")
            update_student(name, grade)
            

        elif operation == 3:
            view_student_details()


        elif operation == 4:
            name = input("Enter students name to be deleted: ").title()
            del_student(name)

        elif operation == 5:
            print("Closing the system....")
            break

        else:
            print("invalid input")



main()

   



    
