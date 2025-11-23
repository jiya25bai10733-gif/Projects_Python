
from info import contacts

def search():
    search_name = input("Enter name to search: ")
    found = False
    for name, c in contacts.items():
        if search_name.lower() in name.lower():
            print(f"Found – Name: {name}, Age: {c['age']}, Phone: {c['phone']}, Email: {c['email']}")
            found = True
    if not found:
        print("No matching contacts found in your contact book!")

