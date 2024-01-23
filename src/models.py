from abc import ABC, abstractmethod
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
    
   
class Users(Model):
    path= "../data/usersMiranda.json"

class Comments(Model):
    path= "../data/commentsMiranda.json"