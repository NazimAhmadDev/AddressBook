# Seacrh and count the persons present in the city 
def search_city_and_count(contacts):
    search_city = input("Enter the city name to search: ").lower()
    count = sum(1 for contact in contacts if contact.city.lower() == search_city)

    if count > 0:
        print(f"\nNumber of persons in '{search_city.title()}': {count}")
    else:
        print(f"\nNo persons found in '{search_city.title()}'.")