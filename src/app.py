import argparse
from models import Users



def runApp():
    parser = argparse.ArgumentParser(
        prog="Pyhton App",
        description= "Manipulate Data from Json")
    parser.add_argument("action", choices=["list_users","view_user","create_user","update_user"])

    args = parser.parse_args()

    if args.action =="list_users":
        Users.list()
    elif args.action =="view_user":
        Users.view()
    elif args.action =="create_user":
        Users.create()
    elif args.action =="update_user":
        Users.update()
    
runApp()