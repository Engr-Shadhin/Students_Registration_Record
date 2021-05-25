"""
            Student's Registration Record

        Hafizur Rahman Shadhin----191-15-12666
        Fazlerabbi Antor----------191-15-12688
        Shukdeb Bhowmik Shuvo-----191-15-12832
        Mst. Shuchana Kabir-------191-15-12769
"""


import csv
student_fields = ['ID', 'Name', 'All Course Code', 'Section', 'Registration Status']
student_database = 'students.csv'




def display_menu():
    print("------------------------------------------")
    print(" Welcome to Student's Registration System")
    print("------------------------------------------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")



def add_student():
    print("-------------------------")
    print("Add Student's Data")
    print("-------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Registration Done")
    input("Press any key to continue")
    return



def view_students():
    global student_fields
    global student_database

    print("--- Student's Registration ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t\t\t\t\t\t|')
        print("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t\t  |")
            print("\n")

    input("Press any key to continue")





def search_student():
    global student_fields
    global student_database

    print("--- Search Student ---")
    ID = input("Please Enter ID to Search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if ID == row[0]:
                    print("----- Student Found -----")
                    print("ID: ", row[0])
                    print("Name: ", row[1])
                    print("Course List: ", row[2])
                    print("Section: ", row[3])
                    print("Registration Status: ", row[4])
                    break
        else:
            print("Sorry ID Not Found")
    input("Press any key to continue")





def update_student():
    global student_fields
    global student_database

    print("--- Update Student ---")
    ID = input("Enter Student's ID to Update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ID == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("ID Not Found")

    input("Press any key to continue")





def delete_student():
    global student_fields
    global student_database

    print("--- Delete Student ---")
    ID = input("Enter ID to delete registration: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ID != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Registration ID ", ID, "delete successfully")
    else:
        print("ID not found")

    input("Press any key to continue")






while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break

print("-----------")
print(" Thank you")
print("-----------")

