from vehicle import EconomyCar, SUV, LuxuryCar
from customer import Customer
from payment import MpesaPayment, CardPayment, CashPayment
from rental_system import CarRentalSystem

system = CarRentalSystem("SafariDrive Rentals")

# Add vehicles
car1 = EconomyCar("KDK 123A", "Toyota", "Axio", 2022, 4000)
car2 = SUV("KDJ 456B", "Toyota", "Prado", 2023, 8000)
car3 = SUV("KDJ 672B", "Nissan", "X-Trail", 2021, 6500)
car4 = LuxuryCar("KDL 789C", "Mercedes-Benz", "E-Class", 2024, 15000)
car5 = EconomyCar("KDM 234D", "Honda", "Fit", 2021, 3500)

for car in [car1, car2, car3, car4, car5]:
    system.add_vehicle(car)

# Register customers
customer1 = Customer(
    "C001", "John Kamau", "0712345678", "12345678", "DL45821"
)
customer2 = Customer(
    "C002", "Jane Wanjiku", "0723456789", "23456789", "DL56832"
)
customer3 = Customer(
    "C003", "Peter Otieno", "0734567890", "34567890", "DL67843"
)

for customer in [customer1, customer2, customer3]:
    system.register_customer(customer)

# Display available vehicles
system.show_available_vehicles()

# Rent the Prado for 4 days
rental1 = system.rent_vehicle(customer1, car2, 4)
rental1.display_rental_details()

# Try to rent the Prado again. This should fail.
try:
    system.rent_vehicle(customer1, car2, 2)
except ValueError as error:
    print(f"Error: {error}")

# Return the Prado 2 days late, then pay using M-Pesa
system.return_vehicle(rental1, actual_days=6)
payment1 = MpesaPayment(rental1, "0712345678")
system.process_payment(payment1)

# Rent and return the Axio, then pay by card
rental2 = system.rent_vehicle(customer2, car1, 3)
system.return_vehicle(rental2, actual_days=3)
payment2 = CardPayment(rental2, "1234")
system.process_payment(payment2)

# Rent and return the Mercedes, then pay by cash
rental3 = system.rent_vehicle(customer3, car4, 2)
system.return_vehicle(rental3, actual_days=2, damage_charge=5000)
payment3 = CashPayment(rental3, rental3.calculate_total() + 1000)
system.process_payment(payment3)

# Display customer rental histories
for customer in [customer1, customer2, customer3]:
    customer.view_rental_history()

# Generate the management report
system.generate_report()
