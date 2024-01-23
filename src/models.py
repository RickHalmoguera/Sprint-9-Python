from abc import ABC, abstractmethod
from datetime import datetime

import json

class Model(ABC):
    def __init__(self,path):
        self.path= path
    
    @classmethod
    def list(cls):
        with open(cls.path) as open_json:
            read_json = open_json.read()
            print (read_json)

    @classmethod
    def view(cls):
        with open(cls.path) as open_json:
            data = json.load(open_json)
            print("Enter the id please")
            id = input()
        
        for element in data:
            if element["id"] == int(id):
                print (element)
    
    @classmethod
    def create(cls):
            with open(cls.path) as open_json:
                data = json.load(open_json)
                json_length = len(data)
                
                current_date = datetime.now().date()
                
                new_user = {
                    "photo": "http://dummyimage.com/88x88.png/5fa2dd/ffffff",
                    "id": json_length + 1,
                    "first_name": input("First Name: "),
                    "last_name": input("Last Name: "),
                    "email": input("Email: "),
                    "start_date": current_date,
                    "job_title": input("Job Title: (Manager, Recepcionist, Room Service) "),
                    "description": input("Job description: "),
                    "phone": input("Phone: "),
                    "is_active": input("Is User Active: (Y/N)").upper() == "Y"
                }
                
                print(f'The new user data is:\n{new_user}')
            
    @classmethod
    
    def update(cls):
        with open(cls.path) as open_json:
            data = json.load(open_json)
            print("Enter the id you want to edit please")
            id = input()
            
        for element in data:
            if element["id"] == int(id):
                
                while True:
                    print(element)
                    property_to_change = input("Enter the property to change or EXIT to exit : ")

                    if property_to_change in element:
                        new_value = input(f"Enter the new value for {property_to_change}: ")
                        element[property_to_change] = new_value
                        print(f'The new user {property_to_change} is:\n{element[property_to_change]}')
                        break  
                    elif property_to_change.upper() == "EXIT":
                        print("Bye!")
                        break    
                    
                    else:
                        print("Property not found! Please enter a valid property.")

class Users(Model):
    path= "../data/usersMiranda.json"

class Comments(Model):
    path= "../data/commentsMiranda.json"