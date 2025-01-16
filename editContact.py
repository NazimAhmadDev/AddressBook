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