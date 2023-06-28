# Ask user whether they want to write a equation into or read equation from selected txt file.
while True:
    try:
        action = input(
            "Do you want to 'write' or 'read' equations ? (write/read) ").lower()

        # Ensure user choose only "write" or "read"
        if action != "write" and action != "read":
            raise Exception()

        break
    except Exception:
        print("Invalid input, please select (write/read)")

# Proceed if user choose to write a equation into a file
if action == "write":
    while True:
        try:
            # user input numbers and operator
            num1 = float(input("Please enter 1st number : "))
            operator = input("Please enter the operator (+ , -, *, /) : ")

            # check valid operator
            if operator != "+" and operator != "-" and operator != "*" and operator != "/":
                raise Exception()

            num2 = float(input("Please enter 2nd number : "))

            # user select which txt file to write into.
            file_name = input(
                "What is the text file name for this equation to write ? ")

            # perform calculation
            if operator == "+":
                ans = num1 + num2
            elif operator == "-":
                ans = num1 - num2
            elif operator == "*":
                ans = num1 * num2
            elif operator == "/":
                ans = num1 / num2
            else:
                ans = "Error"

            # Create the equation in string format
            equation = str(num1) + " " + operator + " " + str(num2) + \
                " " + "=" + " " + str(round(ans, 1))

            # open or create selected file and write equation into it.
            file = None
            file = open(file_name + ".txt", "a+")
            file.write(equation + "\n")
            file.close()

            print("\nEquation has written into " +
                  file_name + ".txt :", equation)

            break

        except ValueError:
            print("That is not a valid number. Please try again...")
        except ZeroDivisionError:
            print("Divided by zero error, please enter over again.")
        except Exception:
            print("Entered operator is not valid, please try again ...")

# proceed if user choose read equation from selected file.
elif action == "read":
    while True:
        try:
            file = None

            # Ask user to pick a txt file
            file_name = input(
                "Please select which txt file to read ? ")

            # open the file and read the contents
            file = open(file_name + ".txt", "r")
            print("\n-----" + file_name + ".txt -----")
            print(file.read())
            break
        except FileNotFoundError as error:
            print("The text file does not exist.")

        # make sure the file will be closed
        finally:
            if file is not None:
                file.close()
