class Rental:
    def __init__(self, rental_id, customer, vehicle, rental_days):
        if rental_days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        self.rental_id = rental_id
        self.customer = customer
        self.vehicle = vehicle
        self.rental_days = rental_days
        self.actual_days = None
        self.status = "ACTIVE"
        self.base_cost = vehicle.calculate_rental_cost(rental_days)
        self.late_fee = 0
        self.damage_charge = 0
        self.__paid = False

    def calculate_late_fee(self):
        if self.actual_days is None:
            return 0

        late_days = max(0, self.actual_days - self.rental_days)
        return late_days * self.vehicle.daily_rate * 0.20

    def calculate_total(self):
        return self.base_cost + self.late_fee + self.damage_charge

    def complete_rental(self, actual_days, damage_charge=0):
        if self.status != "ACTIVE":
            raise ValueError("Only active rentals can be completed.")

        if actual_days <= 0:
            raise ValueError("Actual rental days must be greater than zero.")

        if damage_charge < 0:
            raise ValueError("Damage charge cannot be negative.")

        self.actual_days = actual_days
        self.damage_charge = damage_charge
        self.late_fee = self.calculate_late_fee()
        self.status = "COMPLETED"

    def mark_as_paid(self):
        if self.status != "COMPLETED":
            raise ValueError("Only completed rentals can be paid.")

        if self.__paid:
            raise ValueError("This rental has already been paid.")

        self.__paid = True

    def is_paid(self):
        return self.__paid

    def display_rental_details(self):
        print("Rental ID:", self.rental_id)
        print("Customer:", self.customer.name)
        print("Vehicle:", self.vehicle.make, self.vehicle.model)
        print("Booked days:", self.rental_days)
        print("Actual days:", self.actual_days)
        print("Status:", self.status)
        print(f"Base cost: KSh {self.base_cost:,.2f}")
        print(f"Late fee: KSh {self.late_fee:,.2f}")
        print(f"Damage charge: KSh {self.damage_charge:,.2f}")
        print(f"Total: KSh {self.calculate_total():,.2f}")
        print("Paid:", self.is_paid())