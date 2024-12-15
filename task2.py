
contacts = []
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print(f"Contact for {name} added successfully!\n")
def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("List of Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        print()
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    global contacts
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    print(f"Contact for {name} deleted successfully!\n")
def display_menu():
    print("Contact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")
if __name__ == "__main__":
    main()
