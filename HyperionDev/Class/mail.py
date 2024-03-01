### --- OOP Email Simulator --- ###
"""Simple software to read emails and mark them read, input and clear_screen are 
used in order to help the user with the readibility of the choices"""
import os
def clear_screen():
    """Clearing screen funtion"""
    os.system("cls")

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

    # Declare the class variable, with default value, for emails.
    # Initialise the instance variables for emails.

    # Create the method to change 'has_been_read' emails from False to True.

class Email:
    """Defining the simple class Email"""
    def __init__(self, email_address : str, subject_line : str, email_content : str) -> None:
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    has_been_read: bool = False

    def mark_as_read(self):
        """Mark the mail has read once opened"""
        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.

inbox : Email = []


# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    """This function populates the inbox with some fake emails"""
    # Create 3 sample emails and add it to the Inbox list.
    inbox.append(Email("someemail@someprovider.com",
                       "Welcome to HyperionDev", 
                       "Here a new mail class"))
    inbox.append(Email("anothermail@anotherprovider.com",
                       "Great work on the bootcamp!", 
                       "You're going good!"))
    inbox.append(Email("yetanotheremail@yetanotherprovider.co.uk",
                       "Your excellent marks!", 
                       "Don't give up now"))


def list_emails(unread = False):
    """Listing the emails contained in the inbox, it has to checks in order to 
    allow the code to using the same funtion for the read and unread emails"""
    # Create a function which prints the email’s subject_line, along with a corresponding number.

    for email_number, mail in enumerate(inbox):
        if unread is False:
            print(email_number, mail.subject_line)
        else:
            if mail.has_been_read is False:
                print(email_number, mail.subject_line)
            else:
                continue




def read_email(index):
    """Reading a specific email"""
    clear_screen()
    # Create a function which displays a selected email.
    # Once displayed, call the class method to set its 'has_been_read' variable to True.

    print(f"From:\t\t {inbox[index].email_address}")
    print(f"Subject:\t {inbox[index].subject_line}\n")
    print(f"{inbox[index].email_content}")
    inbox[index].mark_as_read()

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
#menu = True

populate_inbox()

while True:
    clear_screen()
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    if user_choice == 1:
        clear_screen()
        list_emails()
        try:
            mail_selection = int(input("Which email do you want to read? "))
            if mail_selection < 0 or mail_selection > (len(inbox) - 1):
                print("Wrong input")
            else:
                read_email(mail_selection)
                input("Press any button to continue")
                clear_screen()
        except TypeError:
            print("Wrong input, must be a number")

    elif user_choice == 2:
        clear_screen()
        print("Unread emails\n")
        list_emails(True)
        input("\nPress any button to continue")
    elif user_choice == 3:
        break

    else:
        print("Oops - incorrect input.")
