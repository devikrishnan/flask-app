#import sqlite
#conn = sqlite3.connect('todo.db')
#query = "<SQLite Query goes here>"
#result = conn.execute(query)

import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          id INTEGER PRIMARY KEY,
          Title TEXT,
          Description TEXT,
          _is_done boolean DEFAULT 0,
          _is_deleted boolean DEFAULT 0,
          CreatedOn Date DEFAULT CURRENT_DATE,
          DueDate Date,
          UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)

    def create_user_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "User" (
         _Id INTEGER PRIMARY KEY AUTOINCREMENT
         Name TEXT,
         Email TEXT,
         CreatedOn Date DEFAULT CURRENT_DATE,
        );
        """

        self.conn.execute(query)

class ToDoModel:
    TABLENAME = "Todo"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def create(self, text, description,DueDate,UserId):
        query = f'insert into {self.TABLENAME} ' \
                f'(Title, Description,DueDate,UserId) ' \
                f'values ("{text}","{description}","{DueDate}","{UserId}")'
        
        result = self.conn.execute(query)
        return result

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()


    def delete(self, item_id):
        query=f'update{self.TABLENAME}'
              f'SET _is_deleted={1}'
              f'where id={item_id}'

        self.conn.execute(query)
        return self.list_items()


    def update(self,item_id,update_info):
        query=f"UPDATE {self.TABLENAME} " \
              f"SET {Title = update_info.Title, Description=update_info.Description, DueDate= update_info.DueDate } " \
              f"WHERE id = {item_id}"

    def list_items(self, _id):
        query=f"select id, Title, Description, DueDate, is_done" \
              f"from{self.TABLENAME} WHERE _is_deleted !={1} and UserId = _id"
              print (query)
              result=self.conn.execute(query)
              return result







class User:
    TABLENAME = "User"

    def create(self, name, email):
        query = f'insert into {self.TABLENAME} ' \
                f'(Name, Email) ' \
                f'values ({name},{email})'
        result = self.conn.execute(query)
        return result

    
