while True:
    try:
        # ask user to input the number of students
        number_of_student = int(
            input("How many students register the exam ? "))

        # setup a list to store all students' ID
        student_ID = []

        # keep asking for students ID by using for loop.
        # Append all ID into a list
        for i in range(0, number_of_student):
            student_ID.append(input("What is your student ID ? "))

        # open or create the file if not exist.
        with open("reg_form.txt", "w+") as f:
            # loop through all student ID from the list and write them into the file.
            for i in range(0, len(student_ID)):
                f.write(student_ID[i] + "\n\n\n\n\n-------------\n")

        print("All students ID are write into reg_form.txt successfully.")

        break
    except ValueError:
        print("Invalid input. Please try again.")
    except Exception:
        print("Error occur, please restart the program.")
