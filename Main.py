from deleteContact import delete_contact
from duplicateContact import is_duplicate_contact
from editContact import edit_contact
from searchCityandCount import search_city_and_count
from searchPersonByState import search_person_by_state
from sortContactAlphabetically import sort_contacts_alphabetically
from sortContactsByCityOrZip import sort_contacts_by_city_or_zip
import findContactByName, viewAddressBook


class Contact:
    def __init__(self, firstname, lastname, address, city, zip_code, phone_number, email):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email
    
    def __str__(self):
        return f"Name : {self.firstname} {self.lastname}\n" \
            f"Address : {self.address}\n \tCity : {self.city}\n \tZip Code : {self.zip_code}\n" \
            f"Phone : {self.phone_number}\n" \
            f"Email : {self.email}\n"




# Taking contact from User
def get_contacts_from_user(firstname,lastname):
    #firstname = input("Enter first name: ")
    #lastname = input("Enter last name: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    zip_code = input("Enter zip code: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    
    return Contact(firstname, lastname, address, city, zip_code, phone_number, email)


"""
def is_duplicate_contact(contacts, firstname, lastname):
    # Check if a contact with the same first and last name already exists.
    for contact in contacts:
        if contact.firstname.lower() == firstname.lower() and contact.lastname.lower() == lastname.lower():
            return True
    return False
"""


"""
# Find contact by name
def find_contact_by_name(contacts, name):
    for contact in contacts:
        if contact.firstname.lower() == name.lower():
            return contact
    return None
"""


"""
# View addressBook
def view_address_book(contacts):
    if not contacts:
        print("\nThe address book is empty!")
        return

    print("\n********************************* Address Book *********************************")
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}:")
        print(contact)
"""



"""
# Edit contact details
def edit_contact(contact):
    print("\n********************************* Editing Contact *********************************")
    contact.firstname = input(f"Enter new firstname (Current: {contact.firstname}): ") or contact.firstname
    contact.lastname = input(f"Enter new lastname (Current: {contact.lastname}): ") or contact.lastname
    contact.address = input(f"Enter new address (Current: {contact.address}): ") or contact.address
    contact.city = input(f"Enter new city (Current: {contact.city}): ") or contact.city
    contact.zip_code = input(f"Enter new zip code (Current: {contact.zip_code}): ") or contact.zip_code
    contact.phone_number = input(f"Enter new phone number (Current: {contact.phone_number}): ") or contact.phone_number
    contact.email = input(f"Enter new email (Current: {contact.email}): ") or contact.email
"""




"""
# Deleting the contacts
def delete_contact(contacts):
    name_to_delete = input("Enter the first name of the contact to delete: ")
    contact_to_delete = findContactByName.find_contact_by_name(contacts, name_to_delete)

    if contact_to_delete:
        contacts.remove(contact_to_delete)
        print(f"\nContact '{name_to_delete}' has been deleted successfully.")
    else:
        print(f"\nNo contact found with the name '{name_to_delete}'.")
"""



"""
# Seacrh and count the persons present in the city 
def search_city_and_count(contacts):
    search_city = input("Enter the city name to search: ").lower()
    count = sum(1 for contact in contacts if contact.city.lower() == search_city)

    if count > 0:
        print(f"\nNumber of persons in '{search_city.title()}': {count}")
    else:
        print(f"\nNo persons found in '{search_city.title()}'.")
"""




"""
# Sorting the contacts by name
def sort_contacts_alphabetically(contacts):
    contacts.sort(key=lambda contact: contact.firstname.lower())
    print("\n******************* Sorting the contacts A-Z *************************")
    for contact in contacts:
        print(contact)
"""




"""
# Sorting the contacts by city or zipCode
def sort_contacts_by_city_or_zip(contacts):
    sort_by = input("Enter to sort by : ")
    if sort_by == "city":
        print("\n ********************* Sorting by City *************************")
        contacts.sort(key = lambda contact: contact.city.lower())
        for contact in contacts:
            print(contact)

    elif sort_by == "zip code":    
        print("\n ********************* Sorting by zip code *************************")
        contacts.sort(key = lambda contact: contact.zip_code)
        for contact in contacts:
            print(contact)

    else:
        print("Invalid input!!!, Please choose city or zip code")
"""



"""
# Search person by the state
def search_person_by_state(contacts):
    state_to_search = input("Enter city to search: ")
    found_contacts = list(filter(lambda contact: contact.city.lower() == state_to_search.lower(), contacts))

    if found_contacts:
        print(f"\nContacts living in {state_to_search}:")
        for contact in found_contacts:
            print(contact)
    else:
        print(f"\nNo contacts found in the city '{state_to_search}'.")
"""






def manage_contacts(contacts):
    while True:
        print("\nOptions:")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Search Person by City/State")
        print("6. Count Number of persons in particular state")
        print("7. Sort the contacts A-Z")
        print("8. Sort by city/zip_code")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        if choice == "1":
            firstname = input("Enter first name: ")
            lastname = input("Enter last name: ")
            if is_duplicate_contact(contacts, firstname, lastname):
                print(f"\nContact with name {firstname} {lastname} already exists. Cannot add duplicate.")
            else:
                contact = get_contacts_from_user(firstname,lastname)
                contacts.append(contact)
                print("\nContact added successfully!")


        elif choice == "2":
            viewAddressBook.view_address_book(contacts)

        elif choice == "3":
            name_to_edit = input("Enter the first name of the contact to edit: ")
            contact = findContactByName.find_contact_by_name(contacts, name_to_edit)
            if contact:
                edit_contact(contact)
                print("\nContact updated successfully!")
            else:
                print(f"No contact found with the name '{name_to_edit}'.")

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            search_person_by_state(contacts)

        elif choice == "6":
            search_city_and_count(contacts)

        elif choice == "7":
            sort_contacts_alphabetically(contacts)
        
        elif choice == "8":
            sort_contacts_by_city_or_zip(contacts)

        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")





def manage_address_book():
    address_books = {}

    while True:
        print("\nAddress Book Management Menu:")
        print("1. Create a new Address Book")
        print("2. Select an Address Book")
        print("3. View all Address Books")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            address_book_name = input("Enter new address book name: ")
            if address_book_name in address_books:
                print(f"{address_book_name} already exists.")
            else:
                address_books[address_book_name] = []
                print(f"Address book '{address_book_name}' created successfully!")

        elif choice == "2":
            address_book_name = input("Enter address book name: ")
            if address_book_name in address_books:
                manage_contacts(address_books[address_book_name])
            else:
                print(f"No address book found with the name '{address_book_name}'.")

        elif choice == "3":
            if not address_books:
                print("No address books found.")
            else:
                print("\nAvailable Address Books:")
                for name in address_books:
                    print(f"- {name}")

        elif choice == "4":
            print("Exiting the Address Book Program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")


def main():
    manage_address_book()


if __name__ == "__main__":
    main()
