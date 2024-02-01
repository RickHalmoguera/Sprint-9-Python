from abc import ABC, abstractmethod
from datetime import datetime
from connection.connectionToMySQL import connectToDb


class Model(ABC):
    def __init__(self,table):
        self.table = table
   
    @classmethod
    def list(cls):
        db = connectToDb()
        if db:
            try:
                cursor = db.cursor()
                cursor.execute(f'SELECT * FROM {cls.table}')
                tableData = cursor.fetchall()

                print(f'{cls.table} data:')
                for row in tableData:
                    print(row)

            except Exception as e:
                print(f'Cant show data from {cls.table} {e}')

            finally:
                if db.is_connected():
                    db.close()
                    
    @classmethod
    def view(cls):
        id = input(f'id from {cls.table} table:')
        connection = connectToDb()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(f'SELECT * FROM {cls.table} WHERE id={id}')
                tableData = cursor.fetchall()

                if tableData:
                    print('Data {cls.table}: ')
                for row in tableData:
                    print(row)
                    return row
                else:
                    input('Cant find this id')

            except Exception as e:
                print(f'Cant show data from {cls.table} {e}')

            finally:
                if connection.is_connected():
                    connection.close()

    @classmethod
    def create(cls):
        current_date = datetime.now().strftime("%Y-%m-%d")
        new_user = {
            'photo': 'http://dummyimage.com/88x88.png/5fa2dd/ffffff',
            'first_name': input('First Name: '),
            'last_name': input('Last Name: '),
            'job_title': input('Eliga Reception, Manager o Service\n'), 
            'email': input('Email: '), 
            'phone': input('Phone: '), 
            'start_date': current_date,
            'description': input('Job description: ') ,
            'is_active': input('Is User Active: (Y/N)').upper() == 'Y',
        }
        
        print(new_user)
            
class Users(Model):
    table ="users"


