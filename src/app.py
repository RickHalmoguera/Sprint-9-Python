import argparse
from models.models import Users



parser = argparse.ArgumentParser(
    prog="Pyhton App",
    description= "Manipulate Data from MySQL")
parser.add_argument("action", choices=["list_users","view_user","create_user","update_user","list_comments","view_comment","list_rooms","view_room","list_bookings","view_booking"])

args = parser.parse_args()

actions={
    'list_users': Users.list(),
    'view_user' : Users.view()
}

if args in actions:
    actions[args]()
    
