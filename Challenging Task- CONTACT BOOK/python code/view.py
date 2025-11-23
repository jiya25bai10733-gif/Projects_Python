from info import contacts

def view():
    name = input("Enter name to view: ")
    if name in contacts:
        c = contacts[name]
        print(f"Name: {name}, Age: {c['age']}, Phone: {c['phone']}, Email: {c['email']}")
    else:
        print(f"{name} not found in your contact book!")
