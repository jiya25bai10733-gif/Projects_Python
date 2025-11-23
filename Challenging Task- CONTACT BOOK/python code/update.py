import info

def update():
    name = input("Enter name to update: ")
    if name in info.contacts:
        age = input("Enter new age: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        info.contacts[name] = {'age': age, 'phone': phone, 'email': email}
        print(f"Contact with name {name} updated!")
    else:
        print(f"{name} not found!")
