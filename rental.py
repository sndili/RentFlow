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
        from vehicle import SUV, LuxuryCar

        print("====================================")
        print("        SAFARIDRIVE RENTALS")
        print("====================================")
        print(f"Rental ID:        {self.rental_id}")
        print(f"Customer:         {self.customer.name}")
        print(f"Vehicle:          {self.vehicle.make} {self.vehicle.model}")
        print(f"Registration:     {self.vehicle.registration_number}")
        print(f"Rental Period:    {self.rental_days} days")
        print(f"Daily Rate:       KSh {self.vehicle.daily_rate:,.0f}")
        print()

        rental_charge = self.vehicle.daily_rate * self.rental_days
        print(f"Rental Charge:    KSh {rental_charge:,.0f}")

        if isinstance(self.vehicle, SUV):
            print("Service Charge:   KSh  2,000")
        elif isinstance(self.vehicle, LuxuryCar):
            insurance = rental_charge * 0.10
            print(f"Insurance (10%):  KSh {insurance:,.0f}")

        print("------------------------------------")
        print(f"TOTAL:            KSh {self.base_cost:,.0f}")
        print(f"Status:           {self.status}")
        print("====================================")

        if self.status == "COMPLETED":
            print(f"Late Fee:         KSh {self.late_fee:,.0f}")
            print(f"Damage Charge:    KSh {self.damage_charge:,.0f}")
            print(f"Final Total:      KSh {self.calculate_total():,.0f}")

        print("Paid:", self.is_paid())