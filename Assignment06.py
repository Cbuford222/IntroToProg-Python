import json
# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #


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
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

#variables
menu_choice: str = ''
students: list = []

class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function will read students' registration data from a JSON file.

        :param file_name: string for file name
        :param student_data: list of dictionary rows containing student registration
        :return: list of dictionary rows
        """
        try:
            with open(file_name, "r") as file:
                student_data = json.load(file)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script", e)
            student_data = []  # Ensure student_data is initialized as an empty list
        except json.JSONDecodeError as e:
            IO.output_error_messages("Error decoding JSON data", e)
            student_data = []
        except Exception as e:
            IO.output_error_messages("A non-specific error occurred", e)
        finally:
            return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Writes data from list of dictionary rows to a JSON file.

        :param file_name: string with the name of the file
        :param student_data: list you want to save to file
        :return: string with the result of the save
        """
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file, indent=4)  # Added indent for readability
        except TypeError as e:
            IO.output_error_messages("Check that the data is in a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("A non-specific error occurred", e)


class IO:
    """
    A collection of presentation layer functions that manage user input and output
    ChangeLog: (Who, When, What)
    Chloe, 2024-08-07, Created class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays error messages to the user.

        :param message: string with the error message
        :param error: Exception object
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("--Technical Error Message--")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function will display a menu of choices to the user.

        :param menu: string with menu text
        :return: None
        """
        print("\n" + menu + "\n")  # Cleaned up formatting

    @staticmethod
    def input_menu_choice():
        """
        This function gets a menu choice from the user.

        :return: string with the user's choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise ValueError("Please choose only 1, 2, 3, or 4")
        except ValueError as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Displays the collected student data.

        :param student_data: list of dictionary rows
        :return: None
        """
        print("\n" + "-" * 50 + "\n")
        for student in student_data:
            print(f"First Name: {student.get('first_name')}, "
                  f"Last Name: {student.get('last_name')}, "
                  f"Course: {student.get('course')}")
        print("\n" + "-" * 50 + "\n")

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function will get the first name, last name, and course from the user.

        :param student_data: list of dictionary rows
        :return: list of dictionary rows
        """
        try:
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers or special characters")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers or special characters")

            student_course = input("What is the student's course? ")

            # Assuming course can contain any string, if there are specific checks required, they should be added here.

            student = {
                "first_name": student_first_name,
                "last_name": student_last_name,
                "course": student_course
            }
            student_data.append(student)
        except ValueError as e:
            IO.output_error_messages("That value is not the correct kind of data", e)
        except Exception as e:
            IO.output_error_messages("A non-specific error occurred", e)
        return student_data

students = FileProcessor.read_data_from_file(FILE_NAME, students)

while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
    elif menu_choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        IO.output_error_messages("Invalid choice. Please select a valid option.")