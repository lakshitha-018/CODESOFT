class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        print("Contact List:")
        for contact in self.contacts:
            print(f"{contact.name} - {contact.phone_number}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if contact.name.lower().startswith(query.lower()) or contact.phone_number.startswith(query):
                results.append(contact)

        return results

    def search_contact_name(self, query):
        results = []
        for contact in self.contacts:
            if contact.name.lower().startswith(query.lower()) or contact.phone_number.startswith(query):
                results.append(contact)

        return results

    def update_contact(self, contact, name, phone_number, email, address):
        contact.name = name
        contact.phone_number = phone_number
        contact.email = email
        contact.address = address

    def delete_contact(self, contact):
        self.contacts.remove(contact)

def main():
    contact_book = ContactBook()

    while True:
        print("Contact Book Menu:")
        print("[1] Add Contact")
        print("[2] View Contact List")
        print("[3] Search Contact")
        print("[4] Update Contact")
        print("[5] Delete Contact")
        print("[6] Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the contact's name: ")
            phone_number = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email address: ")
            address = input("Enter the contact's address: ")

            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)

            print("Contact added successfully!")

        elif choice == 2:
            contact_book.view_contact_list()

        elif choice == 3:
            query = input("Enter the contact's name or phone number: ")

            results = contact_book.search_contact(query)

            if len(results) > 0:
                print("Search results:")
                for contact in results:
                    print(f"{contact.name} - {contact.phone_number}")
            else:
                print("No contacts found.")

        elif choice == 4:
            name = input("Enter the contact's name : ")

            contact = contact_book.search_contact_name(name)

            if len(contact) > 0:
                contact = contact[0]

                new_name = input("Enter the new name for the contact: ")
                new_phone_number = input("Enter the new phone number for the contact: ")
                new_email = input("Enter the new email address for the contact: ")
                new_address = input("Enter the new address for the contact: ")

                contact_book.update_contact(contact, new_name, new_phone_number, new_email, new_address)

                print("Contact updated successfully!")
            else:
                print("Contact not found.")

        elif choice == 5:
            name = input("Enter the contact's name: ")

            contact = contact_book.search_contact(name)

            if len(contact) > 0:
                contact = contact[0]

                contact_book.delete_contact(contact)

                print("Contact deleted successfully!")
            else:
                print("Contact not found.")

        elif choice == 6:
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()