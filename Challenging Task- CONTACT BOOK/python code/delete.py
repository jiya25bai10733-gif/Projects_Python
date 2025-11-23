import info

def delete():
    name = input("Enter name to delete: ")
    if name in info.contacts:
        del info.contacts[name]
        print(f"Contact {name} deleted!")
    else:
        print(f"{name} not found!")


