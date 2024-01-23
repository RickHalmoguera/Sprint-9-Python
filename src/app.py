import argparse
from models import Users



def runApp():
    parser = argparse.ArgumentParser(
        prog="Pyhton App",
        description= "Manipulate Data from Json")
    parser.add_argument("action", choices=["list_users","view_user"])

    args = parser.parse_args()

    if args.action =="list_users":
        Users.list()
    elif args.action =="view_user":
        Users.view()

    
runApp()