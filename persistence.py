import sqlite3
import atexit
from dbtools import Dao
 
# Data Transfer Objects:
class Employee:
    def __init__(self, id, name, salary, branche):
        super().__init__()
        self.id = id 
        self.name = name
        self.salary = salary
        self.branche = branche

 
class Supplier:
    def __init__(self, id, name, contact_information):
        super().__init__()
        self.id = id
        self.name = name
        self.contact_information = contact_information

class Product:
    def __init__(self, id, description, price, quantity):
        super().__init__()
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity

class Branche:
    def __init__(self, id, location, number_of_employees):
        super().__init__()
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees


class Activitie:
    def __init__(self, product_id, quantity, activator_id, date):
        super().__init__()
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date
 
 
#Repository
class Repository(object):
    def __init__(self):
        self._conn = sqlite3.connect('bgumart.db')
        #TODO: complete
        self.employees = Dao(Employee, self._conn)
        self.suppliers = Dao(Supplier, self._conn)
        self.products = Dao(Product, self._conn)
        self.branches = Dao(Branche, self._conn)
        self.activities = Dao(Activitie, self._conn)
        
        
 
    def _close(self):
        self._conn.commit()
        self._conn.close()
 
    def create_tables(self):
        self._conn.executescript("""
            CREATE TABLE employees (
                id              INT         PRIMARY KEY,
                name            TEXT        NOT NULL,
                salary          REAL        NOT NULL,
                branche    INT REFERENCES branches(id)
            );
    
            CREATE TABLE suppliers (
                id                   INTEGER    PRIMARY KEY,
                name                 TEXT       NOT NULL,
                contact_information  TEXT
            );

            CREATE TABLE products (
                id          INTEGER PRIMARY KEY,
                description TEXT    NOT NULL,
                price       REAL NOT NULL,
                quantity    INTEGER NOT NULL
            );

            CREATE TABLE branches (
                id                  INTEGER     PRIMARY KEY,
                location            TEXT        NOT NULL,
                number_of_employees INTEGER
            );
    
            CREATE TABLE activities (
                product_id      INTEGER REFERENCES products(id),
                quantity        INTEGER NOT NULL,
                activator_id    INTEGER NOT NULL,
                date            TEXT    NOT NULL
            );
        """)

    def execute_command(self, script: str) -> list:
        return self._conn.cursor().execute(script).fetchall()
 
# singleton
repo = Repository()
atexit.register(repo._close)