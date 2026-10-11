from abc import ABC, abstractmethod
import random
import string


class Payment(ABC):
    def __init__(self, rental):
        self.rental = rental
        self.amount = rental.calculate_total()

        if self.amount < 0:
            raise ValueError("Payment amount cannot be negative.")

    @abstractmethod
    def process_payment(self):
        pass


class MpesaPayment(Payment):
    def __init__(self, rental, phone_number):
        super().__init__(rental)
        self.phone_number = phone_number
        self.transaction_code = None

    def process_payment(self):
        if self.rental.status != "COMPLETED":
            raise ValueError("Only completed rentals can be paid.")

        if self.rental.is_paid():
            raise ValueError("This rental has already been paid.")

        characters = string.ascii_uppercase + string.digits
        self.transaction_code = "".join(
            random.choices(characters, k=10)
        )

        print("M-Pesa payment successful.")
        print("Phone number:", self.phone_number)
        print(f"Amount paid: KSh {self.amount:,.2f}")
        print("Transaction code:", self.transaction_code)

        return True


class CardPayment(Payment):
    def __init__(self, rental, last_four_digits):
        super().__init__(rental)

        if (
            not str(last_four_digits).isdigit()
            or len(str(last_four_digits)) != 4
        ):
            raise ValueError("Enter only the last four digits of the card.")

        self.last_four_digits = str(last_four_digits)

    def process_payment(self):
        if self.rental.status != "COMPLETED":
            raise ValueError("Only completed rentals can be paid.")

        if self.rental.is_paid():
            raise ValueError("This rental has already been paid.")

        print("Card payment successful.")
        print("Card ending in:", self.last_four_digits)
        print(f"Amount paid: KSh {self.amount:,.2f}")

        return True


class CashPayment(Payment):
    def __init__(self, rental, amount_received):
        super().__init__(rental)

        if amount_received < 0:
            raise ValueError("Amount received cannot be negative.")

        self.amount_received = amount_received

    def process_payment(self):
        if self.rental.status != "COMPLETED":
            raise ValueError("Only completed rentals can be paid.")

        if self.rental.is_paid():
            raise ValueError("This rental has already been paid.")

        if self.amount_received < self.amount:
            print("Cash payment failed. Insufficient amount received.")
            print(f"Amount due: KSh {self.amount:,.2f}")
            print(f"Amount received: KSh {self.amount_received:,.2f}")
            return False

        change = self.amount_received - self.amount

        print("Cash payment successful.")
        print(f"Amount due: KSh {self.amount:,.2f}")
        print(f"Amount received: KSh {self.amount_received:,.2f}")
        print(f"Change: KSh {change:,.2f}")

        return True