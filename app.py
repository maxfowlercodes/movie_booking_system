BOOKING_FEE = 75
films = ["Night Harbour", "Paper Lions", "Ice Road"]
seats_left = [65, 2, 10]
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

show_films(films)
movie = int(input("What movie would you like to see? "))
if movie == 1 or movie == 2 or movie == 3:
    wanted = int(input("How many people will be coming? "))
    for i in range(wanted):
        age = int(input(f"Enter the age of person number {wanted}: "))
        overall_price = overall_price + ticket_price(age)
    if can_book(seats_left, wanted, movie) == True:
        print(f"Can be booked, price is {overall_price:.2f}")
    else:
        print("Sorry there is not enough seats left. ")



