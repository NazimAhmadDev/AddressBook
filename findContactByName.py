# Find contact by name
def find_contact_by_name(contacts, name):
    for contact in contacts:
        if contact.firstname.lower() == name.lower():
            return contact
    return None