# Problem 1a

# prompt for total sales target
target = float(input("Enter total sales target: "))

cumulative_sales = 0.0

# 5‑day week using for loop
for day in range(1, 6):
    day_sales = float(input(f"Enter day {day} sales: "))
    cumulative_sales = cumulative_sales + day_sales
    percent = (cumulative_sales / target) * 100
    print(f"Cumulative sales: {cumulative_sales} ({percent} %)")


# Problem 1b

valid_target = False
while not valid_target:
    try:
        target = float(input("Enter total sales target: "))
        if target <= 0:
            print("Sales target must be greater than 0.")
        else:
            valid_target = True
    except ValueError:
        print("Invalid input. Please enter a numeric value for the sales target.")

cumulative_sales = 0.0

for day in range(1, 6):
    valid_day_sales = False
    while not valid_day_sales:
        try:
            day_sales = float(input(f"Enter day {day} sales: "))
            if day_sales <= 0:
                print("Sales must be greater than 0.")
            else:
                valid_day_sales = True
        except ValueError:
            print("Invalid input. Please enter a numeric value for the sales.")

    cumulative_sales = cumulative_sales + day_sales
    percent = (cumulative_sales / target) * 100
    print(f"Cumulative sales: {cumulative_sales} ({percent} %)")


# Problem 2a and 2c combined

fastest_route_number = 0
fastest_time_minutes = 0.0

route_number = 1
more_routes = "y"

while more_routes == "y":
    # get valid distance
    valid_distance = False
    while not valid_distance:
        try:
            distance = float(input(f"Enter route {route_number} distance (miles): "))
            if distance <= 0:
                print("Distance must be greater than 0.")
            else:
                valid_distance = True
        except ValueError:
            print("Invalid input. Please enter a numeric value for distance.")

    # get valid speed
    valid_speed = False
    while not valid_speed:
        try:
            speed = float(input(f"Enter route {route_number} speed (miles/hour): "))
            if speed <= 0:
                print("Speed must be greater than 0.")
            else:
                valid_speed = True
        except ValueError:
            print("Invalid input. Please enter a numeric value for speed.")

    # compute time in minutes: time_hours = distance / speed
    time_hours = distance / speed
    time_minutes = time_hours * 60

    print(f"Route {route_number} time: {time_minutes:.0f} minutes")

    # update fastest route
    if route_number == 1 or time_minutes < fastest_time_minutes:
        fastest_time_minutes = time_minutes
        fastest_route_number = route_number

    # ask if there are more routes
    more_routes = input("More routes (y/n)?: ").lower()
    while more_routes != "y" and more_routes != "n":
        more_routes = input("Please enter 'y' or 'n': ").lower()

    route_number = route_number + 1

print(f"Route {fastest_route_number} is fastest; {fastest_time_minutes:.0f} minutes")

# Problem 2b - Running the code with table information
# Local route distance (miles): 30
# Local route speed (miles/hour): 30
# Local route time: 60 minutes

# Parkway route distance (miles): 35
# Parkway route speed (miles/hour): 40
# Parkway route time: 52 minutes

# Enter Highway route distance (miles): 48
# Enter Highway route speed (miles/hour): 55
# Highway route time: 52 minutes

# The code will say Highway route is fastest at 52 minutes, but Parkway is also tied at 52 minutes