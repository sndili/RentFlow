class Customer:
    def __init__(self, customer_id, name, phone_number, national_id, driving_licence):
        if not driving_licence or not driving_licence.strip():
            raise ValueError("A customer must have a valid driving licence.")

        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.national_id = national_id
        self.driving_licence = driving_licence
        self.rentals = []

    def display_details(self):
        print("Customer ID:", self.customer_id)
        print("Name:", self.name)
        print("Phone number:", self.phone_number)
        print("National ID:", self.national_id)
        print("Driving licence:", self.driving_licence)

    def add_rental(self, rental):
        self.rentals.append(rental)

    def view_rental_history(self):
        print("\nRental History for", self.name)

        if not self.rentals:
            print("No rental history found.")
            return

        for rental in self.rentals:
            print(
                "Rental ID:", rental.rental_id,
                "| Vehicle:", rental.vehicle.make, rental.vehicle.model,
                "| Status:", rental.status
            )
