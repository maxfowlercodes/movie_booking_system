import time
BOOKING_FEE = 75
films = ["Night Harbour", "Paper Lions", "Ice Road"]
seats_left = [65, 2, 10]
prices = []
price_per_person = []
overall_price = 0


def show_films(films):
    for i in range(len(films)):
        print(f"{i + 1}. {films[i]}")


def ticket_price(age):
    if age < 16:
        return 550 + BOOKING_FEE
    elif age >= 65:
        return 600 + BOOKING_FEE
    else:
        return 850 + BOOKING_FEE


def can_book(seats_left, wanted, movie):
    if seats_left[movie - 1] - wanted >= 0:

        return True
    else:
        return False

def average_price_system(prices, overall_price, price_per_person, wanted):
    for i in range(wanted):
        print(f"Age: {price_per_person[i]}  - Price: £{prices[i]}")
    print(f"Average price per person is: £{round(overall_price / len(prices))}")

show_films(films)
movie = int(input("What movie would you like to see? "))
if movie == 1 or movie == 2 or movie == 3:
    wanted = int(input("How many people will be coming? "))
    for i in range(wanted):
        age = int(input(f"Enter the age of person number {i + 1}: "))
        time.sleep(1.2)
        overall_price = overall_price + ticket_price(age)
        prices.append(ticket_price(age))
        price_per_person.append(age)
    if can_book(seats_left, wanted, movie) == True:
        print(f"Can be booked, price is £{overall_price}")
        time.sleep(1)
        average_price_system(prices, overall_price, price_per_person, wanted)
        time.sleep(1.5)
        print("-" * 20)
        print("BOOKING PROCCESSING")
        print("-" * 20)
        time.sleep(2)
        seats_left[movie - 1] - wanted
        print("")
        print("Your booking has been succesfully made.")
        print(f"There is {seats_left[movie - 1]} seats left after your booking. ")
    else:
        print("Sorry there is not enough seats left. ")


