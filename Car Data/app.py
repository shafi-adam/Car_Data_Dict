import database

USER_CHOICE = """
Enter:

- 'a' to add a new car
- 'l' to list all cars
- 's' to search for a car
- 'd' to delete a car
- 'p' to update car price
- 'q' to quit

Your choice: """

# Add car
def prompt_add_car():
    name = input("Enter car name: ")
    country = input("Enter car country: ")
    year = int(input("Enter publication year: "))
    price = float(input("Enter car price: "))
    
    database.insert_car(name,country,year,price)

# List cars
def list_cars():
    cars = database.get_all_cars()

    for car in cars:
        print(
            f"{car['name']} by {car['country']} "
            f"| Year: {car['year']} "
            f"| Price: ${car['price']}"
        )


# Search car
def prompt_search_car():
    name = input("Enter car name: ")
    car = database.search_car(name)

    if car:
        print("\ncar Found!")
        print(f"Name   : {car['name']}")
        print(f"country : {car['country']}")
        print(f"Year   : {car['year']}")
        print(f"Price  : ${car['price']}")
    else:
        print("car not found!")


# Delete car
def prompt_delete_car():
    name = input("Enter the car name to delete: ")
    database.delete_car(name)


# Update Price
def prompt_update_price():
    name = input("Enter car name: ")
    new_price = float(input("Enter new price: "))

    database.update_price(name,new_price)

def menu():
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input == "a":
            prompt_add_car()
        elif user_input == "l":
            list_cars()
        elif user_input == "s":
            prompt_search_car()
        elif user_input == "d":
            prompt_delete_car()
        elif user_input == "p":
            prompt_update_price()
        else:
            print("Invalid choice!")

        user_input = input(USER_CHOICE)

menu()