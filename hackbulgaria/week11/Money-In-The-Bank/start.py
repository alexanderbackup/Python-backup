from sql_manager import *
from getpass import getpass


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = getpass(prompt="Enter your password: ")
            try:
                register(username, password)
            except PasswrodError:
                print('''
                Password needs to:
                    - be at least 8 symbols long !
                    - has uppercase character !
                    - has at least one special symbol !
                ''')

            print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass(prompt="Enter your password: ")

            logged_user = login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass(prompt="Enter your new password: ")
            change_pass(logged_user, new_pass)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())
            
        elif command == 'exit':
            break

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("exit - for exiting")


def main():
    create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
