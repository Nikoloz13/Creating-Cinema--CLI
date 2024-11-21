from common import process_user_input
from db import sessions

def list_user_menu_items():
    print("1. list sessions")
    print("2. search movie")
    print("3. book tickets")
    print("4. my tickets")
    print("5. back")
    return process_user_input()

def greetings():
    print("Hello!!! ")
    print("How may i help you? ")

def search_movie():
    print("Search session")
    if sessions == []:
        print("There is no session to search!!! ")
        return
    
    search_season = (input("Enter the Film name to search: "))

    for session in sessions:
        if session["film_name"] == search_season:
            print("We have the session on this film! ")
            print(f"\tSession ID: {session['session_id']}")
            print(f"\tFilm name: {session['film_name']}")
            print(f"\tStart time: {session['start_time']}")
            print(f"\tRoom number: {session['room_number']}")
            print(f"\tRoom length: {session['room_length']}")
            print(f"\tRoom width: {session['room_width']}")
            print(f"\tCapacity: {session['capacity']}")
        else:    
            print("We have no session on this film, sorry! ")
        


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
    


def user_panel():
    greetings()
    while True:
        user_input = list_user_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":    
                search_movie()
            case "3":    
                print("Booking Tickets")
            case "4":
                print("My tickets")
            case "5":
                print("returning to main menu...")
                break    
            case "exit":
                print("GoodBye!")
                exit()
            case _:
                print("Invalid Input")  