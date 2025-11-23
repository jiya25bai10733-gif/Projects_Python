from create import create
from view import view
from update import update
from delete import delete
from search import search
from count import Count

while True:
    print("\nContact Book Manager")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create()
    elif choice == '2':
        view()
    elif choice == '3':
        update()
    elif choice == '4':
        delete()
    elif choice == '5':
        search()
    elif choice == '6':
        Count()
    elif choice == '7':
        print("Exiting...Closing the program")
        break
    else:
        print("Invalid choice! Try again.")

