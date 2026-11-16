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


