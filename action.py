from persistence import *

import sys

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            #TODO: apply the action (and insert to the table) if possible
            
            #this all from the actions input file
            product_id = int(splittedline[0]) #gets the id of the product
            quantity = int(splittedline[1]) #gets the quantity of the action
            activator_id = int(splittedline[2]) #if quantity<0 than its an employee Id. if quantity>0 its supplier Id
            date = splittedline[3]
            
            # Get current product quantity, before the action
            product = repo.products.find(id=product_id)[0]
            
            # For sales (quantity<0), check if enough product in stock
            if quantity < 0 and abs(quantity) > product.quantity:
                continue
            
            # Update product quantity
            product.quantity += quantity   #if its a sale quantity<0 and the amount lowers else it a but so there are more
            repo.products.delete(id=product_id)
            repo.products.insert(product)
            
            
            #creates a new activity and inserts to the table
            activity = Activitie(product_id, quantity, activator_id, date)
            repo.activities.insert(activity)    

if __name__ == '__main__':
    main(sys.argv)
    
    
    
    
            
           