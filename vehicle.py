from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, registration_number, make, model, year, daily_rate):
        if daily_rate < 0:
            raise ValueError("Daily rate cannot be negative.")

        self.registration_number = registration_number
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.__available = True

    def is_available(self):
        return self.__available

    def mark_as_rented(self):
        self.__available = False

    def mark_as_available(self):
        self.__available = True

    def display_details(self):
        status = "Available" if self.is_available() else "Rented"

        print(f"Registration: {self.registration_number}")
        print(f"Vehicle: {self.make} {self.model}")
        print(f"Year: {self.year}")
        print(f"Daily rate: KSh {self.daily_rate:,.2f}")
        print(f"Status: {status}")

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass


class EconomyCar(Vehicle):
    def __init__(self, registration_number, make, model, year, daily_rate):
        super().__init__(registration_number, make, model, year, daily_rate)

    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        return self.daily_rate * days


class SUV(Vehicle):
    def __init__(self, registration_number, make, model, year, daily_rate):
        super().__init__(registration_number, make, model, year, daily_rate)

    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        service_charge = 2000
        return (self.daily_rate * days) + service_charge


class LuxuryCar(Vehicle):
    def __init__(self, registration_number, make, model, year, daily_rate):
        super().__init__(registration_number, make, model, year, daily_rate)

    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        insurance = self.daily_rate * days * 0.10
        return (self.daily_rate * days) + insurance
