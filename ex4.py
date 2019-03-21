# This is telling me how many cars there is
cars = 100
# This is going to tell me how much space there is in a car
space_in_a_car = 40
# This is telling me how many drivers there is for the 100 cars
drivers = 30
# This is telling how many passengers there is
passengers = 90
# This tells me how many empty cars there is going to be so you have to substract how many cars there is by how many drivers there is available
cars_not_driven = cars - drivers
# How many cars are going to be driven base on how many drivers there is
cars_driven = drivers
# To find the carpool capacity, I am going to multiply how many cars are going to be driven by the space in the car
carpool_capacity = cars_driven * space_in_a_car
# This is telling me how many average passengers is going to be in 1 car
average_passengers_per_car = passengers / cars_driven

# The print is going to tell me how many cars are available
print("There are", cars, "cars available.")
# The print is going to tell me how many drivers is available to drive the cars
print("There are", drivers, "drivers available.")
# This print is going to tell me how many cars are empty
print("There will be", cars_not_driven, "empty cars today.")
# This print is going to tell me how many people will be able to fit in one car
print("We can transport", carpool_capacity, "people today.")
# The print is telling me how many passengers I have today
print("We have", passengers, "to carpool today.")
# This print is going to average the passengers per car
print("We need to put about", average_passengers_per_car, "in each car.")
# _ is called an underscore character and it is used a lot to put an imaginary space between words in variable names