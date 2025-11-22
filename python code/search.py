from info import contacts

def search():
    search_name = input("Enter name to search from your contact book: ")
    found = False
    for name, c in contacts.items():
        if search_name.lower() in name.lower():
            print(f"Found – Name: {name}, Age: {cage}, Phone: {phone}, Email: {email}")
            found = True
    if not found:
        print("No contact found!")
