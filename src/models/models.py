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
                cursor = db.cursor(dictionary=True)
                cursor.execute(f'SELECT * FROM {cls.table}')
                tableData = cursor.fetchall()

                print(f'{cls.table} data:')
                for row in tableData:
                    for key, value in row.items():
                            print(f'{key}: {value}')

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
                    print(f'Data {cls.table}: ')
                    for row in tableData:
                        for key, value in row.items():
                            print(f'{key}: {value}')
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
        
    @classmethod
    def update(cls):
        data_user = Users.view()
        id = data_user['id']
        active_status = 'YES' if data_user['is_active'] == 1 else 'NO'
        user = {
            'photo': data_user['photo'],
            'first_name': input(f'First Name: ({data_user['first_name']})') or data_user['first_name'],
            'last_name': input(f'Last Name: ({data_user['last_name']})') or data_user['last_name'],
            'job_title': input(f'Job Title: ({data_user['job_title']})') or data_user['job_title'],
            'email': input(f'Email: ({data_user['email']})') or data_user['email'],
            'phone': input (f'Phone: ({data_user['phone']})') or data_user['phone'],
            'startDate': data_user['start_date'],
            'description': input(f'Job description: ({data_user['description']})') or data_user['description'],
            'is_active': input(f'Is User Active: (Y/N) ({active_status})').upper() == 'Y' or data_user['is_active'],
            }
        print(user)
            
    @classmethod
    def delete(cls):
        id = input('Id you want to delete: ')

        connection = connectToDb()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(f'DELETE FROM {cls.table} WHERE id = {id}')
                connection.commit()              
                print(f'User {id} was deleted')

            except Exception as e:
                print(f'There was an error during process: {e}')

            finally:
                if connection.is_connected():
                    connection.close()
                    
class Users(Model):
    table ="users"


