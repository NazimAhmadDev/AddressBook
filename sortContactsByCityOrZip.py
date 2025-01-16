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