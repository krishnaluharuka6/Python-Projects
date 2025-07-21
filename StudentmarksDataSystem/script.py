import pandas as pd;
import json


students={

}


def add_student(name,sub_grade):
    with open("C:/Users/Dell/Desktop/KRISHNA_WORK/python/projects/StudentmarksDataSystem/students.json","r+") as f:
        students = json.load(f)
        students[name] = sub_grade
        students[name]["Total"]= sum(sub_grade.values())
        students[name]["Average"] = students[name]["Total"]/5
        topper = []
        max=0
        for n, marks in students.items():
            if max<marks["Total"]:
                max = marks["Total"]
                topper.clear()
                topper.append(n)
            elif max==marks["Total"]:
                topper.append(n)


        print(f'Total : {students[name]["Total"]}')
        print(f'Average: {students[name]["Average"]}')
        print(f"The Topper is {topper}")
        f.seek(0)
        json.dump(students, f, indent=4)
        f.truncate()
    print(f"Student details added Successfully")

def view_details():
    with open("C:/Users/Dell/Desktop/KRISHNA_WORK/python/projects/StudentmarksDataSystem/students.json","r") as f:
        students = json.load(f)
        df = pd.DataFrame(students)
        print(df)

def update_details():
    name = input("Enter student name to update: ").title()
    with open("C:/Users/Dell/Desktop/KRISHNA_WORK/python/projects/StudentmarksDataSystem/students.json","r+") as f:
        students = json.load(f)
        if name in students:
            print(f"Your Grades: {students[name]}")
            changed_subject = input("Enter the subject to update ").title()
            if changed_subject in students[name]:
                while True:
                    try:
                        changed_grade = float(input("Enter grade"))
                        if 0 <= changed_grade <= 100:
                            break  # Exit loop if valid
                        else:
                            print("Grade must be between 0 and 100.")
                    except ValueError:
                        print("Please enter a numeric value.")

               
                students[name][changed_subject] = changed_grade
                sub=["Maths","Science","Nepali","Social","Computer"]
                marks = [marks for subject,marks in students[name].items() if subject in sub]
                total = sum(marks)
                students[name]["Total"] = total
                students[name]["Average"] = total/5
                topper = []
                max=0
                for n, marks in students.items():
                    if max<marks["Total"]:
                        max = marks["Total"]
                        topper.clear()
                        topper.append(n)
                    elif max==marks["Total"]:
                        topper.append(n)
                print(f'Total : {students[name]["Total"]}')
                print(f'Average: {students[name]["Average"]}')
                print(f"The Topper is {topper}")
                f.seek(0)
                json.dump(students, f, indent=4)
                f.truncate()
                print(f"Student details updated Successfully")
            else:
                print("This subject doesn't exist")
        else:
            print("The student doesn't exist")



def delete_details(name):
    with open("C:/Users/Dell/Desktop/KRISHNA_WORK/python/projects/StudentmarksDataSystem/students.json","r+") as f:
        students = json.load(f)
        if name in students:
            del students[name]
            f.seek(0)
            json.dump(students, f, indent=4)
            f.truncate()
            print("Deleted the details of student successfully")
        else:
            print("The student doen't exist")




def main():
    while True:
        print("""Enter
1 to add student grades
2 to update
3 to view
4 to delete
5 to exit from the System \n """)
        try:
            operation = int(input())

            if operation == 1:
                name = input("Enter name of the student: ").title()
                while name.isalpha() == False:
                    print("Name of student can be alphabet only. Please eneter name properly")
                    name = input("Enter name of the student: ").title()
                grade = {}
                for i in ["Maths","Science","Nepali","Social","Computer"]:
                    while True:
                            try:
                                grade[i] = float(input(f"Enter grade of the student in {i} "))
                                if 0 <= grade[i] <= 100 and name.isalnum():
                                    break  # Exit loop if valid
                                else:
                                    print("Grade must be between 0 and 100.")
                            except ValueError:
                                print("Please enter a numeric value for grade")    
                add_student(name, grade)
                

            elif operation == 2:
                update_details()
                

            elif operation == 3:
                view_details()



            elif operation == 4:
                name = input("Enter students name to be deleted: ").title()
                while name.isalpha() == False:
                    print("Name of student can be alphabet only. Please eneter name properly")
                    name = input("Enter name of the student to be deleted: ").title()
                delete_details(name)

            elif operation == 5:
                print("Closing the system....")
                break

            else:
                print("invalid input")
        
        except ValueError:
            print("Please enter the number between 1 to 5")

main()