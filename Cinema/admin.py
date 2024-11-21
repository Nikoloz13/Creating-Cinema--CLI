from common import process_user_input
from random import randint
from db import sessions


def list_admin_menu_items():
    print("1. list all sessions")
    print("2. remove session")
    print("3. add session")
    print("4. edit session")
    print("5. back")
    return process_user_input()

def greetings():
    print("Welcome to the admin panel")
    print("Please sign in to continue")

def add_session():
    print("Adding session")
    print("Enter the session details")
    film_name = input("Film name: ")
    start_time = input("Start Time: ")
    room_number = input("Room number: ")
    room_length = int(input("Room length: "))
    room_width = int(input("Room width: "))
    capacity = room_length * room_width
    session_id = randint(1, 1000)
    session = {
        "session_id": session_id,
        "film_name": film_name,
        "start_time": start_time,
        "room_number": room_number,
        "room_length": room_length,
        "room_width": room_width,
        "capacity": capacity
    }
    print("Session added successfully! ")
    sessions.append(session)


def list_sessions():
    print("Listing sessions")
    if sessions == []:
        print("There is no sessions!!!")
    for session in sessions:
        print(f"Session ID: {session['session_id']}")
        print(f"\tFilm name: {session['film_name']}")
        print(f"\tStart time: {session['start_time']}")
        print(f"\tRoom number: {session['room_number']}")
        print(f"\tRoom length: {session['room_length']}")
        print(f"\tRoom width: {session['room_width']}")
        print(f"\tCapacity: {session['capacity']}")


def remove_session():
    print("Remove session")
    if sessions == []:
        print("There is no session to remove!!! ")
        return
    
    session_id_to_remove = int(input("Enter the session ID to remove: "))

    for session in sessions:
        if session["session_id"] == session_id_to_remove:
            sessions.remove(session)
            print(f"Session with ID {session_id_to_remove} has been removed.")
            break
        print("Invalid Session ID")


def edit_session():
    print("Edit session")
    if not sessions:
        print("There are no sessions to edit!")
        return

    session_id_to_edit = int(input("Enter the session ID to edit: "))

    for session in sessions:
        if session["session_id"] == session_id_to_edit:
            print(f"Editing session with ID {session_id_to_edit}")
            print(f"Current room size: {session['room_length']} x {session['room_width']} (Capacity: {session['capacity']})")

            new_length = int(input("Enter new room length: "))
            new_width = int(input("Enter new room width: "))

            if new_length > session["room_length"] or new_width > session["room_width"]:
                session["room_length"] = new_length
                session["room_width"] = new_width
                session["capacity"] = new_length * new_width
                print(f"Room size updated! New size: {new_length} x {new_width} (Capacity: {session['capacity']})")
            else:
                print("New dimensions must be greater than the current dimensions to increase the size.")
            return  

    print(f"No session found with ID {session_id_to_edit}.")


def admin_loop():
    greetings()
    while True:
        user_input = list_admin_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":    
                remove_session()
            case "3":    
                add_session()
            case "4":
                edit_session()
            case "5":
                print("returning to main menu...")
                break    
            case "exit":
                print("GoodBye!")
                exit()
            case _:
                print("Invalid Input")