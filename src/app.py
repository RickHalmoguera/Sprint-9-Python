import argparse
from models.models import Users



parser = argparse.ArgumentParser(
    prog='Pyhton App',
    description= 'Manipulate Data from MySQL')
parser.add_argument('action', choices=['list_users','view_user','create_user','update_user','delete_user'])

args = parser.parse_args()

user_choice = args.action
actions={
    'list_users': Users.list,
    'view_user' : Users.view,
    'delete_user': Users.delete,
    'update_user': Users.update,
    'create_user' : Users.create
}

if user_choice in actions:
    actions[user_choice]()
    
