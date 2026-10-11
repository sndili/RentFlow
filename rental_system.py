from vehicle import SUV
from rental import Rental


class CarRentalSystem:
    def __init__(self, name="SafariDrive Rentals"):
        self.name = name
        self.vehicles = []
        self.customers = []
        self.rentals = []
        self.payments = []
        self.__revenue = 0

    @property
    def revenue(self):
        return self.__revenue

    def add_vehicle(self, vehicle):
        for existing_vehicle in self.vehicles:
            if existing_vehicle.registration_number == vehicle.registration_number:
                raise ValueError("A vehicle with this registration number already exists.")

        self.vehicles.append(vehicle)

    def register_customer(self, customer):
        for existing_customer in self.customers:
            if existing_customer.customer_id == customer.customer_id:
                raise ValueError("A customer with this ID is already registered.")

        self.customers.append(customer)

    def find_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                return vehicle

        return None

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer

        return None

    def show_available_vehicles(self):
        print("\nAvailable Vehicles")

        found_vehicle = False

        for vehicle in self.vehicles:
            if vehicle.is_available():
                vehicle.display_details()
                print()
                found_vehicle = True

        if not found_vehicle:
            print("No vehicles are currently available.")

    def search_vehicles(self, vehicle_type=None, max_daily_rate=None):
        matching_vehicles = []

        for vehicle in self.vehicles:
            matches_type = (
                vehicle_type is None
                or (
                    isinstance(vehicle_type, type)
                    and isinstance(vehicle, vehicle_type)
                )
                or (
                    isinstance(vehicle_type, str)
                    and type(vehicle).__name__.lower() == vehicle_type.lower()
                )
            )

            matches_rate = (
                max_daily_rate is None
                or vehicle.daily_rate <= max_daily_rate
            )

            if matches_type and matches_rate and vehicle.is_available():
                matching_vehicles.append(vehicle)

        return matching_vehicles

    def rent_vehicle(self, customer, vehicle, days):
        if customer not in self.customers:
            raise ValueError("Customer must be registered before renting.")

        if vehicle not in self.vehicles:
            raise ValueError("Vehicle must belong to the rental fleet.")

        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        if not vehicle.is_available():
            raise ValueError("This vehicle is already rented.")

        rental_id = f"R{len(self.rentals) + 1:03d}"

        rental = Rental(rental_id, customer, vehicle, days)

        vehicle.mark_as_rented()
        self.rentals.append(rental)
        customer.add_rental(rental)

        print(f"Rental {rental_id} created successfully.")
        print(f"Vehicle: {vehicle.make} {vehicle.model}")
        print(f"Booked days: {days}")
        print(f"Base cost: KSh {rental.base_cost:,.2f}")

        return rental

    def return_vehicle(self, rental, actual_days, damage_charge=0):
        if rental not in self.rentals:
            raise ValueError("Rental does not belong to this rental system.")

        if rental.status != "ACTIVE":
            raise ValueError("Only active rentals can be returned.")

        if rental.vehicle.is_available():
            raise ValueError("This vehicle is not currently rented.")

        rental.complete_rental(actual_days, damage_charge)
        rental.vehicle.mark_as_available()

        print(f"\nRental {rental.rental_id} completed.")
        print(f"Late fee: KSh {rental.late_fee:,.2f}")
        print(f"Damage charge: KSh {rental.damage_charge:,.2f}")
        print(f"Total due: KSh {rental.calculate_total():,.2f}")

        return rental

    def process_payment(self, payment):
        rental = payment.rental

        if rental not in self.rentals:
            raise ValueError("Rental does not belong to this rental system.")

        if rental.status != "COMPLETED":
            raise ValueError("Only completed rentals can be paid.")

        if rental.is_paid():
            raise ValueError("This rental has already been paid.")

        if payment.amount < 0:
            raise ValueError("Payment amount cannot be negative.")

        if payment.amount != rental.calculate_total():
            raise ValueError("Payment amount must match the rental total.")

        successful = payment.process_payment()

        if successful:
            rental.mark_as_paid()
            self.payments.append(payment)
            self.__revenue += payment.amount
            print(f"SafariDrive Rentals revenue: KSh {self.revenue:,.2f}")

        return successful

    def show_active_rentals(self):
        print("\nActive Rentals")

        found_rental = False

        for rental in self.rentals:
            if rental.status == "ACTIVE":
                rental.display_rental_details()
                print()
                found_rental = True

        if not found_rental:
            print("No active rentals.")

    def show_completed_rentals(self):
        print("\nCompleted Rentals")

        found_rental = False

        for rental in self.rentals:
            if rental.status == "COMPLETED":
                rental.display_rental_details()
                print()
                found_rental = True

        if not found_rental:
            print("No completed rentals.")

    def generate_report(self):
        total_vehicles = len(self.vehicles)
        available_vehicles = sum(
            1 for vehicle in self.vehicles if vehicle.is_available()
        )
        rented_vehicles = total_vehicles - available_vehicles
        total_customers = len(self.customers)
        total_rentals = len(self.rentals)

        active_rentals = sum(
            1 for rental in self.rentals if rental.status == "ACTIVE"
        )
        completed_rentals = sum(
            1 for rental in self.rentals if rental.status == "COMPLETED"
        )
        suv_count = sum(
            1 for vehicle in self.vehicles if isinstance(vehicle, SUV)
        )

        print(f"\n===== {self.name} Report =====")
        print("Total vehicles:", total_vehicles)
        print("Available vehicles:", available_vehicles)
        print("Rented vehicles:", rented_vehicles)
        print("SUVs in fleet:", suv_count)
        print("Registered customers:", total_customers)
        print("Total rentals:", total_rentals)
        print("Active rentals:", active_rentals)
        print("Completed rentals:", completed_rentals)
        print("Successful payments:", len(self.payments))
        print(f"Total revenue: KSh {self.revenue:,.2f}")
        print("==============================")
