from persistence import *

def print_all_tables():
    # Print activities
    print("Activities")
    activities = repo.activities.find_all()
    activities.sort(key=lambda x: x.date)
    for activity in activities:
        print(tuple([activity.product_id, activity.quantity, activity.activator_id, activity.date]))
    
    print("Branches")
    branches = repo.branches.find_all()
    branches.sort(key=lambda x: x.id)
    for branch in branches:
        print(tuple([branch.id, branch.location, branch.number_of_employees]))
    
    print("Employees")
    employees = repo.employees.find_all()
    employees.sort(key=lambda x: x.id)
    for employee in employees:
        print(tuple([employee.id, employee.name, employee.salary, employee.branche]))
        
    print("Products")
    products = repo.products.find_all()
    products.sort(key=lambda x: x.id)
    for product in products:
        print(tuple([product.id, product.description, product.price, product.quantity]))
        
    print("Suppliers")
    suppliers = repo.suppliers.find_all()
    suppliers.sort(key=lambda x: x.id)
    for supplier in suppliers:
        print(tuple([supplier.id, supplier.name, supplier.contact_information]))
        
                        
        
def print_employees_report():
    print("Employees report")
    # Get all employees and sort by name
    employees = repo.employees.find_all()
    employees.sort(key=lambda x: x.name)
        
    for employee in employees:
        # Get branch location
        branch = repo.branches.find(id=employee.branche)[0]
            
        # Calculate total sales income
        total_sales = 0
        activities = repo.activities.find(activator_id=employee.id)
        for activity in activities:
            if activity.quantity < 0:  # Only count sales (negative quantities)
                product = repo.products.find(id=activity.product_id)[0]
                total_sales += abs(activity.quantity) * product.price
                    
        print(f"{employee.name} {employee.salary} {branch.location} {total_sales}")

def print_activities_report():
    print("Activities report")
    
    # Get all activities sorted by date
    activities = repo.activities.find_all()
    activities.sort(key=lambda x: x.date)
    
    for activity in activities:
        # Get product description
        product = repo.products.find(id=activity.product_id)[0]
        
        # Get seller/supplier name
        if activity.quantity < 0:  # Sale
            employee = repo.employees.find(id=activity.activator_id)[0]
            seller_name = employee.name
            supplier_name = "None"
        else:  # Supply
            supplier = repo.suppliers.find(id=activity.activator_id)[0]
            seller_name = "None"
            supplier_name = supplier.name
            
        print(f"('{activity.date}', '{product.description}', {activity.quantity}, '{seller_name}', '{supplier_name}')")

def main():
    #TODO: implement
    print_all_tables()
    print_employees_report()
    print_activities_report()

if __name__ == '__main__':
    main()