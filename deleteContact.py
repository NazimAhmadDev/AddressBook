import findContactByName

# Deleting the contacts
def delete_contact(contacts):
    name_to_delete = input("Enter the first name of the contact to delete: ")
    contact_to_delete = findContactByName.find_contact_by_name(contacts, name_to_delete)

    if contact_to_delete:
        contacts.remove(contact_to_delete)
        print(f"\nContact '{name_to_delete}' has been deleted successfully.")
    else:
        print(f"\nNo contact found with the name '{name_to_delete}'.")