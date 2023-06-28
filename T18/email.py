### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email(object):

    # Declare the class variable, with default value, for emails.
    has_been_read = False

    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.

    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.
Inbox = []

# --- Functions --- #
# Build out the required functions for your program.


def populate_inbox():

    # Create 3 sample emails and add it to the Inbox list.
    email_a = Email("abc@gmail.com", "Welcome to HyperionDev!",
                    "first email content")
    email_b = Email("def@gmail.com",
                    "Great work on the bootcamp!", "second email content")
    email_c = Email("ght@gmail.com", "Your excellent marks!",
                    "third email content")
    Inbox = [email_a, email_b, email_c]
    return (Inbox)


def list_emails():

    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for count, email in enumerate(Inbox, 0):
        print(f"\t{count} - {email.subject_line}")


def read_email(index):

    # Create a function which displays a selected email.
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    email = Inbox[index]
    print(f"\nFrom:\t\t{email.email_address}")
    print(f"Subject:\t{email.subject_line}")
    print(f"Content:\t{email.email_content}")

    email.mark_as_read()
    print(f"\nEmail from {email.email_address} marked as read.\n")

# --- Email Program --- #


# Call the function to populate the Inbox for further use in your program.
Inbox = populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while menu:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    if user_choice == 1:
        # add logic here to read an email
        print(f"\n--- Emails in your Inbox ---")
        list_emails()
        print(f"------")
        index = int(
            input("\nWhich email do you want to read ? (please enter the index number)"))
        read_email(index)

    elif user_choice == 2:
        # add logic here to view unread emails
        # count the unread emails, if unread_email is zero, meaning user has read all emails in inbox.
        unread_email = 0
        print(f"\n--- Unread emails in your Inbox ---")
        for count, email in enumerate(Inbox, 0):
            if email.has_been_read == False:
                unread_email += 1
                print(f"{count}\t{email.subject_line}")
        if unread_email == 0:
            print(f"You have read all emails in inbox.")
        print(f"------")

    elif user_choice == 3:
        # add logic here to quit appplication
        print(f"\n--- Goodbye ! ---")

        # quit the while loop
        menu = False
    else:
        print("Oops - incorrect input.")

# quit the program
quit()
