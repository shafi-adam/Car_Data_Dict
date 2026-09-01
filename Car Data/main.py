from fastapi import FastAPI
import database

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "car Management API"
    }

@app.get("/cars")
def get_cars():

    return database.get_all_cars()


@app.get("/cars/{name}")
def search_car(name: str):

    car = database.search_car(name)

    if car:

        return car

    return {
        "message": "car not found!"
    }


@app.post("/cars")
def add_car(
    name: str,
    country: str,
    year: int,
    price: float
):

    database.insert_car(
        name,
        country,
        year,
        price
    )

    return {
        "message": "car added successfully!"
    }


@app.delete("/cars/{name}")
def delete_car(name: str):

    result = database.delete_car(name)

    if result:

        return {
            "message": "car deleted successfully!"
        }

    return {
        "message": "car not found!"
    }


@app.put("/cars/{name}/price")
def update_price(
    name: str,
    new_price: float
):

    result = database.update_price(
        name,
        new_price
    )

    if result:

        return {
            "message": "Price updated successfully!"
        }

    return {
        "message": "car not found!"
    }