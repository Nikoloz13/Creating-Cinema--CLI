from admin import admin_loop
from user import user_panel

def list_menu_items():
    print("1. User")
    print("2. Admin")
    return input("->: ").strip().lower()
    
def user_or_admin():
    user_input = input("->: ").lower()
    if user_input not in ["1", "2", "exit"]:
        print("Invalid Input")
        return user_or_admin()
    return user_input    

def greetings():
    print("Welcome to the movie ticket booking system")
    print("Enter whether you are user or admin?")
    print("Please enter EXIT to exit")

def program_loop():
    while True:
        user_input = list_menu_items()
        match user_input:
            case "1":
                user_panel()
            case "2":    
                admin_loop()
            case "exit":
                print("GoodBye!")
                exit()    
            case _:
                print("Invalid Input")    

def main():
    greetings()
    program_loop()
    

if __name__ == "__main__":
    main()