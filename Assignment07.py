# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Chloe Buford>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ""  # Hold the choice made by the user.

# Classes


class Person:
    def __init__(self, student_first_name: str = "", student_last_name: str = ""):
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name


class Student(Person):
    def __init__(self, student_first_name: str = "", student_last_name: str = "", course_name: str = ""):
        super().__init__(student_first_name=student_first_name, student_last_name=student_last_name)
        self.course_name = course_name


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.loads(file)
                for student in list_of_dictionary_data:
                    student_object = Student(student_first_name=student["FirstName"],
                                             student_last_name=student["LastName"],
                                             course_name=student["CourseName"])
                    student_data.append(student_object)
                print("Data was successfully read from file")
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script", e)
        except Exception as e:
            IO.output_error_messages("There was a non specific error", e)
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            list_of_dictionary_data = []
            for student in student_data:
                student_json = {"FirstName": student.student_first_name,
                                "LastName": student.student_last_name,
                                "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)
                with open(file_name, "w") as file:
                    json.dump(list_of_dictionary_data, file)
            print("Data was successfully read from file")
        except TypeError as e:
            IO.output_error_messages("Please check to see if data is in a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("A non specific error occurred", e)


# Presentation --------------------------------------- #
class IO:

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        if error:
            print(f"ERROR: {message} \n{error}")
        else:
            print(f"ERROR: {message}")

    @staticmethod
    def output_menu(menu: str):
        print(MENU)

    @staticmethod
    def input_menu_choice():
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ").strip()

            #  checking if choice is valid
            if choice not in ("1","2","3","4"):  # Valid menu options
                raise Exception("Invalid choice! Please only choose 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())   # Avoiding technical errors

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        print()
        print("-" * 50)
        for student in student_data:
            print(f'{student.student_first_name} {student.student_last_name} registered for {student.course_name}')
        print("-" * 50)
        print()

    @staticmethod
    def input_student_data(student_data: list):
        try:
           student = Student()
           student.student_first_name = input("What is the student's first name? ")
           student.student_last_name = input("What is the student's last name? ")
           student.course_name = input("What is the course name? ")
           student_data.append(student)
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data")
        except Exception as e:
            IO.output_error_messages("A non specif error occurred")
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # registering student for course
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
