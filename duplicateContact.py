def is_duplicate_contact(contacts, firstname, lastname):
    # Check if a contact with the same first and last name already exists.
    for contact in contacts:
        if contact.firstname.lower() == firstname.lower() and contact.lastname.lower() == lastname.lower():
            return True
    return False