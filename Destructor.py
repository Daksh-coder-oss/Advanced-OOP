#Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!

class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Employee deleted")
def create_employee():
    obj=Employee()
    return obj
obj1=create_employee()
print(obj1)

