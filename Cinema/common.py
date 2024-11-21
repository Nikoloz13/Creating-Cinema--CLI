def process_user_input():
    user_input = input("->: ").lower()
    if user_input not in ["1", "2", "3", "4", "5", "exit"]:
        print("Invalid Input")
        return process_user_input()
    return user_input