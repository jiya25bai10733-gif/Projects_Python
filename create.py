from info import contacts

def create():
    name = input("Enter name to be added: ")
    if name in contacts:
        print(f"Contact with name {name} already exists!")
    else:
        age = input("Enter age: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contacts[name] = {'age': age, 'phone': phone, 'email': email}
        print(f"Contact with name {name} added successfully!")