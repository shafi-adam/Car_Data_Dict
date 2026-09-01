# 🚗 Car Management API

A simple **REST API for managing cars** built using **Python and FastAPI**.

This project allows users to add cars, view all cars, search for a specific car, update the car price, and delete a car.

## 🛠️ Technologies Used

* Python
* FastAPI
* Uvicorn
* REST API
* Swagger UI

## 📋 Car Information

The project manages cars using the following details:

| Field   | Description                     |
| ------- | ------------------------------- |
| Name    | Name of the car                 |
| Country | Country associated with the car |
| Year    | Car year                        |
| Price   | Price of the car                |

The car information is stored in a Python list using dictionaries.

## ✨ Features

* Add a new car
* View all cars
* Search for a specific car
* Update car price
* Delete a car
* Interactive API documentation using Swagger UI

## 📂 Project Structure

```text
Car-Management-API/
│
├── main.py
├── database.py
├── app.py
├── car_store.ipynb
├── api methods.txt
└── README.md
```

## ⚙️ Installation

First, install the required packages:

```bash
pip install fastapi uvicorn
```

The project uses **FastAPI** to create the REST API and **Uvicorn** to run the application.

## ▶️ Run the Project

Run the FastAPI application using:

```bash
python -m uvicorn main:app --reload
```

The FastAPI application is created in `main.py` using `FastAPI()`.

The server will start at:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI provides automatic interactive documentation using **Swagger UI**.

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

You can test the API endpoints directly from Swagger UI.

## 🔗 API Endpoints

### 1. Home

**GET**

```text
/
```

Returns a message confirming that the Car Management API is running.

Example response:

```json
{
    "message": "car Management API"
}
```

### 2. Get All Cars

**GET**

```text
/cars
```

Returns all cars available in the application.

This endpoint uses the `get_all_cars()` function from `database.py`.

### 3. Search for a Car

**GET**

```text
/cars/{name}
```

Example:

```text
/cars/Toyota
```

Returns the details of the selected car.

If the car is not found, the API returns:

```json
{
    "message": "car not found!"
}
```

The search function compares the car name without considering uppercase or lowercase letters.

### 4. Add a Car

**POST**

```text
/cars
```

Required parameters:

```text
name
country
year
price
```

Example:

```text
/cars?name=Toyota&country=Japan&year=2024&price=25000
```

This adds a new car to the car list.

### 5. Update Car Price

**PUT**

```text
/cars/{name}/price
```

Example:

```text
/cars/Toyota/price?new_price=28000
```

This updates the price of the selected car.

### 6. Delete a Car

**DELETE**

```text
/cars/{name}
```

Example:

```text
/cars/Toyota
```

This removes the selected car from the car list.

## 🧪 Example

Suppose a car is added with the following details:

```text
Name    : Toyota
Country : Japan
Year    : 2024
Price   : ₹25,000
```

If you send:

```text
PUT /cars/Toyota/price?new_price=28000
```

The price will be updated to:

```text
Toyota → Price: ₹28,000
```

The `update_price()` function searches for the car and changes its price.

## 🖥️ Command-Line Application

The project also contains an `app.py` file that provides a command-line menu.

Available options are:

```text
'a' → Add a new car
'l' → List all cars
's' → Search for a car
'd' → Delete a car
'p' → Update car price
'q' → Quit
```

The menu calls the corresponding functions from `database.py`.

## 🚀 Future Enhancements

The project can be improved by adding:

* Database integration
* Stock availability
* Pydantic data validation
* User authentication
* JWT authentication
* MySQL/PostgreSQL support
* Frontend interface
* Docker deployment
* Cloud deployment

## 👨‍💻 Author

**Shaik Adam Shafi**

B.Tech – Computer Science and Engineering

## 📄 License

This project is created for educational and learning purposes.
