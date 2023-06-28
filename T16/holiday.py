# Define the dictionary for cost look up
cost = {
    'hotel_per_night': 150,
    'car_per_day': 50,
    'flight': {
        'london': 500,
        'hong kong': 700,
        'new york': 600
    }
}

# define all functions for cost calculation


def hotel_cost(num_nights):
    return num_nights * cost["hotel_per_night"]


def plane_cost(city_flight):
    # look up the flight cost by inputed designation directly
    return cost["flight"][city_flight]


def car_rental(rental_days):
    return rental_days * cost["car_per_day"]


def holiday_cost(num_nights, rental_days, city_flight):
    return hotel_cost(num_nights) + car_rental(rental_days) + plane_cost(city_flight)


while True:
    try:
        # Ask user to input all information
        city_flight = input(
            "Where you are planning to ('London / Hong Kong / New York') ? ").lower()

        # check if user inputed designation is in the option provided.
        while city_flight not in cost["flight"]:
            raise Exception()

        num_nights = int(
            input("How many nights you will be staying at a hotel ? "))
        rental_days = int(input("How many days you will be hiring a car ? "))

        # output the result
        print("\n----Cost detail----")
        print(f"Your designtion is : \t\t{city_flight.title()}")
        print(f"You will stay : \t\t{num_nights} nights")
        print(f"You will a car for : \t\t{rental_days} days")
        print(f"Total cost for flight : \t{plane_cost(city_flight)}")
        print(f"Total cost for hotel : \t\t{hotel_cost(num_nights)}")
        print(f"Total cost for car rental : \t{car_rental(rental_days)}")
        print(
            f"Total cost for holiday : \t{holiday_cost(num_nights, rental_days, city_flight)}")

        break

    # check all exception
    except ValueError:
        print("Invalid input, please try again.")
    except Exception:
        print("Designation can only be 'London' / 'Hong Kong' / 'New York', please select one.")
