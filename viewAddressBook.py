def view_address_book(contacts):
    if not contacts:
        print("\nThe address book is empty!")
        return

    print("\n********************************* Address Book *********************************")
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}:")
        print(contact)