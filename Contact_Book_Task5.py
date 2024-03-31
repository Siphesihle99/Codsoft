class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self,contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print("Contact book  is empty")
        else:
            print("Contact List")
            for idx, contact in enumerate(self.contacts):
                print(f"{idx +1}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")

    def search_contact(self,query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number or query in contact.email or query in contact.address:
                found_contacts.append(contact)
        return found_contacts

    def modify_contacts(self, name, new_contact):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.name = new_contact.name
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                break
            else:
                print("contact not found")

    def del_contact(self, name):
        for idx, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[idx]
                print(f"{name} is deleted successfuly.")
                break
            else:
                print("contact not found")

def main():
    contact_book =ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add new contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Modify Contact")
        print("5. Delete Contact")
        print("6. Exit")

        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            name = input("Enter name: ")
            phone = input("Enter your phone number: ")
            email = input("Enter your email: ")
            address= input("Enter your address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)
            print("Contact Saved!")

        elif user_choice == 2:
            contact_book.display_contacts()

        elif  user_choice == 3:
            query = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(query)
            if found_contacts:
                print("contact found:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
            else: print("No matching contact found")

        elif  user_choice == 4:
            query = input("Enter contact name to modify : ")
            found_contacts = contact_book.search_contact(query)
            if found_contacts:
                new_name = input("Enter new name: ")
                new_email = input("Enter new email: ")
                new_phone = input("Enter new phone number: ")
                new_address = input("Enter new address: ")
                new_contact = Contact(new_name, new_phone, new_email, new_address)
                contact_book.modify_contacts(name, new_contact)
                print("Successfuly Modified!")
            else:
                print("contact not found")

        elif  user_choice == 5:
            name = input("Enter name of contact to delete: ")
            contact_book.del_contact(name)
           

        elif user_choice == 6:
            print("Application closed!")
            break

        else:
            print("Invalid choice. Please enter valid choice")

if __name__ == "__main__":
        main()


            
