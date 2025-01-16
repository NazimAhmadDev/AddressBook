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