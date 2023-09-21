class Student:
    def __init__(self, Name, Roll_no, Marks):
        self.Name = Name
        self.Roll_no = Roll_no
        self.Marks = Marks

    def accept_student_data(self):
        Name = input("Enter Student Name: ")
        Roll_no = int(input("Enter Student Roll: "))
        Marks = int(input("Enter Student Marks: "))
        student = Student(Name, Roll_no, Marks)
        student_list.append(student)

    def display_student_details(self, student):
        print("Name:", student.Name)
        print("Roll no:", student.Roll_no)
        print("Marks:", student.Marks)
        print()

    def search_student_details(self, roll_no):
        for i, student in enumerate(student_list):
            if student.Roll_no == roll_no:
                return i
        return -1

    def delete_student_details(self, roll_no):
        index = self.search_student_details(roll_no)
        if index != -1:
            del student_list[index]
            print("Deletion Successful!")
        else:
            print("Student not found!")

student_list = []

while True:
    print("Enter the task you want to perform:")
    print("1. Accept Data")
    print("2. Display Data")
    print("3. Search Data")
    print("4. Delete Data")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj = Student('', 0, 0)
        obj.accept_student_data()
    elif choice == 2:
        print("List of Students:\n")
        for student in student_list:
            obj.display_student_details(student)
    elif choice == 3:
        roll_no = int(input("Enter the roll number of the student you want to search: "))
        index = obj.search_student_details(roll_no)
        if index != -1:
            obj.display_student_details(student_list[index])
        else:
            print("Student not found!")
    elif choice == 4:
        roll_no = int(input("Enter the roll number of the student you want to delete: "))
        obj.delete_student_details(roll_no)
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
