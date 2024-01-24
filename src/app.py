import argparse
from models import Users, Comments, Rooms, Bookings



def runApp():
    parser = argparse.ArgumentParser(
        prog="Pyhton App",
        description= "Manipulate Data from Json")
    parser.add_argument("action", choices=["list_users","view_user","create_user","update_user","list_comments","view_comment","list_rooms","view_room","list_bookings","view_booking"])

    args = parser.parse_args()

    if args.action =="list_users":
        Users.list()
    elif args.action =="view_user":
        Users.view()
    elif args.action =="create_user":
        Users.create()
    elif args.action =="update_user":
        Users.update()
    elif args.action =="list_comments":
        Comments.list()
    elif args.action =="view_comment":
        Comments.view()
    elif args.action =="list_rooms":
        Rooms.list()
    elif args.action =="view_room":
        Rooms.view()
    elif args.action =="list_bookings":
        Bookings.list()
    elif args.action =="view_booking":
        Bookings.view()
    
runApp()