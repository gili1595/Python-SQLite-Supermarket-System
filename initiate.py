from persistence import *

import sys
import os

def add_branche(splittedline : list[str]):
    #TODO: add the branch into the repo
    branch = Branche(
        id=int(splittedline[0]), 
        location=splittedline[1],
        number_of_employees=int(splittedline[2]))
    repo.branches.insert(branch)

def add_supplier(splittedline : list[str]):
    #TODO: insert the supplier into the repo
    supplier = Supplier(
        id=int(splittedline[0]), 
        name=splittedline[1], 
        contact_information=splittedline[2])
    repo.suppliers.insert(supplier)

def add_product(splittedline : list[str]):
    #TODO: insert product
    product = Product(
        id=int(splittedline[0]), 
        description=splittedline[1], 
        price=float(splittedline[2]), 
        quantity=int(splittedline[3]))
    repo.products.insert(product)

def add_employee(splittedline : list[str]):
    #TODO: insert employee
    employee = Employee(
        id=int(splittedline[0]), 
        name=splittedline[1], 
        salary=float(splittedline[2]), 
        branche=int(splittedline[3]))
    repo.employees.insert(employee)

adders = {  "B": add_branche,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    # uncomment if needed
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
        
    #their implementaion  
    repo.__init__()
    repo.create_tables()
    
    #my idea: 
    #   global repo
    #   repo = Repository()
    #   repo.create_tables()
    
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])
        
           

if __name__ == '__main__':
    main(sys.argv)