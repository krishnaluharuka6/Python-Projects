import os

def create_file(filename):
    try:
        with open(f'C:/Users/Dell/Desktop/KRISHNA_WORK/python/projects/FileManagementApp/{filename}','x') as file:
            print(f"Filename {filename}: Created successfully!")
    except FileExistsError:
        print(f"Filename already exist")

    except Exception as e:
        print("An error occurred")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found")
    else:
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove('C:/Users/Dell/Desktop/KRISHNA_WORK/python/projects/FileManagementApp/{filename}')
        print(f"{filename} has been deleted successfully")
    except FileNotFoundError:
        print("File Not found")
    except Exception:
        print("An error occured")


def read_file(filename):
    try:
        with open(f'C:/Users/Dell/Desktop/KRISHNA_WORK/python/projects/FileManagementApp/{filename}','r') as f:
            content = f.read()
            print(f"Content of '{filename}': \n {content}")
    except FileNotFoundError:
        print("Filename doesn't exist")
    except Exception:
        print("An error occured!")

def edit_file(filename):
    try:
        with open(f'C:/Users/Dell/Desktop/KRISHNA_WORK/python/projects/FileManagementApp/{filename}','a') as file:
            content = input("Enter data to add = ")
            file.write(content + "\n")
            print(f"Content added to {filename} Successfully!")

    except FileNotFoundError:
        print("File Not Found")

    except Exception:
        print("An error occured")


def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1: Create File")
        print("2: View all File")
        print("3: Delete File")
        print("4: Read File")
        print("5: Edit File")
        print("6: Exit")

        choice = int(input("Enter your Choice "))

        if choice == 1:
            filename= input("Enter the file name to create ")
            create_file(filename)

        elif choice == 2:
            view_all_files()

        elif choice == 3:
            file_name = input("Enter the name of file you want to delete ")
            delete_file(file_name)

        elif choice == 4:
            filename= input("Enter the file name to read ")
            read_file(filename)

        elif choice == 5:
            filename= input("Enter the file name to edit ")
            edit_file(filename)


        elif choice == 6:
            print("Closing the system...")
            break

        else:
            print("please enter valid choice! ")





main()



        


