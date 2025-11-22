from info import contacts

def delete():
    name = input("Enter name to delete from your contact book: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact with name {name} deleted!")
    else:
        print(f"{name} not foundin your contact book!")
