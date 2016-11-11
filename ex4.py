cars = 100
space_in_car = 4.0
drivers =  30
passenger = 90
cars_not_driven = cars - drivers
cars_driven = drivers
car_pool_capacity = cars_driven * space_in_car
average_passenger_per_car = passenger / cars_driven

print("Total driven cars :",cars)
print("Number of drivers avaialble :", drivers)
print("Number of empty cars : ",cars_not_driven)
print("Total people that can be transported :",car_pool_capacity)
print("Passengers in carpool :",passenger)
print("Average passenger per car :",average_passenger_per_car)