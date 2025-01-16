# Sorting the contacts by name
def sort_contacts_alphabetically(contacts):
    contacts.sort(key=lambda contact: contact.firstname.lower())
    print("\n******************* Sorting the contacts A-Z *************************")
    for contact in contacts:
        print(contact)