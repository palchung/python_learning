# setup two lists to store the 'name' and 'birthday' from the txt file.
name = []
birthday = []

# open the file using 'with/as'
with open("./DOB.txt", "r") as f:

    # loop through every lines from the file
    for line in f:
        # trim all newline to make the result tidy and split the line into each words
        person = line.replace('\n', '').split(" ")

        # join the first two words (the full name), and append it into 'name'
        name.append(" ".join(person[0:2]))

        # join the last three words (the birthday), and append it into 'birthday'
        birthday.append(" ".join(person[2:5]))

    # loop through 'name', and print the contents
    print("Name")
    for i in range(0, len(name)):
        print(name[i])

    # loop through 'birthday', and print the contents
    print("Birthday")
    for i in range(0, len(birthday)):
        print(birthday[i])
