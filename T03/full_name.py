full_name = input("Please enter your full name: ")

if full_name == "":
    print("Please enter your full name.")
elif len(full_name) < 4:
    print("Please make sure that you have entered your name and surname.")
elif len(full_name) > 25:
    print("Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")
