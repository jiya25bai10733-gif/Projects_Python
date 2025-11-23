import info

def view():
    name = input("Enter name to view: ")
    if name in info.contacts:
        c = info.contacts[name]
        print(f"Name: {name}, Age: {c['age']}, Phone: {c['phone']}, Email: {c['email']}")
    else:
        print(f"{name} not found in your contact book!")
