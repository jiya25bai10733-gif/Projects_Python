from info import contacts

def view():
    name = input("Enter name to view from your contact book: ")
    if name in contacts:
        c = contacts[name]
        print(f"Name: {name}, Age: {age}, Phone: {phone}, Email: {email}")
    else:
        print(f"contact with name {name} not found!")