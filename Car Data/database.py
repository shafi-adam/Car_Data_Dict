cars = []

def insert_car(name, country, year, price):

    car = { "name": name, "country": country, "year": year, "price": price }

    cars.append(car)
    print("car added successfully!")


def get_all_cars():
    return cars


def search_car(name):

    for car in cars:

        if car["name"].lower() == name.lower():
            return car

    return None


def delete_car(name):

    for car in cars:

        if car["name"].lower() == name.lower():

            cars.remove(car)
            print("car deleted successfully!")

            return

    print("car not found!")


def update_price(name, new_price):

    car = search_car(name)

    if car:
        car["price"] = new_price
        print("Price updated successfully!")
        return True

    else:
        print("car not found!")
        return False