import info

def search():
    search_name = input("Enter name to search: ")

    if search_name in info.contacts:
        c = info.contacts[search_name]
        print(f"Found – Name: {search_name}, Age: {c['age']}, Phone: {c['phone']}, Email: {c['email']}")
    else:
        print(f"{search_name} not found in your contact book!")

