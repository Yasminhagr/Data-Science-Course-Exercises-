# Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name
# object initializes id and name dynamically for every Employee object created.

# emp = Employee(1, "coder")
# Use del property to first delete id attribute and then the entire object

class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id  
    def display(self):
        print(f"emplyee name is: {self.name} and id: {self.id}")
    
emp1=employee("john", 123)

emp1.display()
del emp1.id
try:
    print(emp1.id)
except NameError:
    print("id attribute is deleted")
del emp1
try:
    print(emp1.display())    
except NameError:
    print("emp1 object is deleted")

