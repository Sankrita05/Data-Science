class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental_cost(self, days):
        # Default calculation based on rental rate
        return days * self.rental_rate


class Car(Vehicle):
    def __init__(self, model, rental_rate, seats):
        super().__init__(model, rental_rate)
        self.seats = seats

    def calculate_rental_cost(self, days):
        # Override the method to calculate cost based on seats, days, and rental rate
        return self.seats * days * self.rental_rate


# Write your code here
# Read input
model = input()
rental_rate, seats, rental_days = map(int, input().split())


# Create a Car object
car = Car(model, rental_rate, seats)

# Calculate and display the rental cost
cost = car.calculate_rental_cost(rental_days)
print(cost)
