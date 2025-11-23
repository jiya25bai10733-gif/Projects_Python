from info import contacts

def create():
    name = input("Enter name: ")
    if name in contacts:
        print(f"contact with name {name} already exists!")
    else:
        age = input("Enter age: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contacts[name] = {'age': age, 'phone': phone, 'email': email}
        print(f"Contact {name} added successfully to your contact book!")
