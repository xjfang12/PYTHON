<<<<<<< HEAD
cars = 100
space_in_a_car = 4.0
drivers = 30.0

passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars ,"Cars available")
print ("There are only", drivers, "drivers available")
print ("There will be", cars_not_driven, "empty_cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today")
=======
cars = 100
space_in_a_car = 4.0
drivers = 30.0

passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars ,"Cars available")
print ("There are only", drivers, "drivers available")
print ("There will be", cars_not_driven, "empty_cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today")
>>>>>>> 2e988e5953e37978d1ddd41d49b7acfffc11b0b1
print ("We need to put about",average_passengers_per_car, "in each car")