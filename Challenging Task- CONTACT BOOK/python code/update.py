
from info import contacts

def update():
    name = input("Enter name to update: ")
    if name in contacts:
        age = input("Enter new age: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        contacts[name] = {'age': age, 'phone': phone, 'email': email}
        print(f"Contact with name {name} updated in your contact!")
    else:
        print(f"{name} not found!")
