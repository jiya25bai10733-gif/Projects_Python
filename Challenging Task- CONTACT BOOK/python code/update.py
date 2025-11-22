from info import contacts

def update():
    name = input("Enter name to update: ")
    if name in contacts:
        age = input("Enter age: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contacts[name] = {'age': age, 'phone': phone, 'email': email}
        print(f"Contact with name {name} updated!")
    else:
        print(f"Contact with name {name} not found!")