"""Calculate the user's total holiday cost, including the plane, hote and car-rental costs"""
import os


def clear_screen():
    """Clearing screen funtion"""
    os.system("cls")




def display_cities():
    """Function that displays the cities that an user can travel to with this agency"""
    print("list of cities present in our database that you can travel to\n")
    print("City\tPrice" )
    for cities_key, cost in cities_costs.items():
        print(cities_key + "\t" + str(cost))


def gathering_user_input():
    """Collecting all the user requirements for the trip"""
    number_of_checks = 1
    city_flight = ""
    number_nights = -1
    rental_days = -1
    while number_of_checks <= 3:
        if number_of_checks == 1:
            display_cities()
            try:
                city_flight = str(input("In which city are you flying? ")) \
                                .strip().lower().capitalize()
                print("\n")
                if city_flight in cities_costs:
                    number_of_checks += 1
            except ValueError:
                print("The city is not valid or not in our database, enter again")
        if number_of_checks == 2:
            try:
                number_nights = int(input("How many nights are you planning to stay? "))
                if number_nights < 1:
                    print("Your stay should be longer minimum 1 day")
                else:
                    number_of_checks += 1
            except ValueError:
                print("Invalid entry, try again")
        if number_of_checks == 3:
            try:
                rental_days = int(input("How many days are you renting a car? "))
                if rental_days < 0:
                    print("Your rental should be 0 or more days")
                else:
                    number_of_checks += 1
            except ValueError:
                print("Invalid entry")

    return city_flight, number_nights, rental_days


def hotel_cost(number_nights):
    """Calculate the total cost for the hotel"""
    check : bool = False
    while not check:
        try:
            hotel_price = int(input("Insert the hotel price per night? "))
            if hotel_price <= 0:
                print("Minimum price should be bigger than 0")
            else:
                check = True
        except ValueError:
            print("Wrong input")
    total_cost = hotel_price * number_nights
    return total_cost


def plane_cost(city_flight):
    """Retrieving the price of the city flight"""
    return int(cities_costs[str(city_flight)])


def car_rental(rental_days):
    """Car service price"""
    check : bool
    car_cost = 0
    #Ternary operation in order to check if the user is renting a car or not
    check = RENTAL_DAYS <= 0 #True if RENTAL_DAYS <= 0 else False
    while not check:
        try:
            car_cost = int(input("What is the price of the car service rental? "))
            if car_cost <= 0:
                print("Minimum price should be bigger than 0")
            else:
                check = True
        except ValueError:
            print("Wrong input")
    return car_cost * rental_days


def holiday_cost(hotel_cost, plane_cost, car_rental):
    """Calculating the whole cost plus showing the flight details"""
    clear_screen()
    print("You are flying to " + str(CITY_FLIGHT))
    print("The total cost of the hotel is " + str(hotel_cost))
    print("The flight costs " + str(plane_cost))
    print("The cost of your car is " + str(car_rental))
    total_cost = hotel_cost + plane_cost + car_rental
    return total_cost



#DEFINING THE CITIES THAT AN USER CAN TRAVEL TO AND THE RESPECTIVE PRICES
cities_costs = {"London" : 120, "Paris" : 80, "Rome" : 100, "Madrid" : 40}
#DEFINING VARIABLE
CITY_FLIGHT : str
NUMBER_OF_NIGHTS : int
RENTAL_DAYS : int


#Gathering all the entry by calling the function
CITY_FLIGHT, NUMBER_OF_NIGHTS, RENTAL_DAYS = gathering_user_input()
#Printing the total cost

print("The total cost of your holiday is " + \
      str(holiday_cost(hotel_cost(NUMBER_OF_NIGHTS),\
                   plane_cost(CITY_FLIGHT),\
                    car_rental(RENTAL_DAYS))))
