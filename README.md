# RentFlow: Car Rental Management System

## 1. Project Overview

RentFlow is a Python-based car rental management system developed for SafariDrive Rentals, a car rental company in Kenya. The system demonstrates how Object-Oriented Programming (OOP) can be used to manage vehicles, customers, rentals, returns, payments and business revenue. The project replaces manual record-keeping with a structured program that helps staff identify available vehicles, manage customer rental histories, calculate rental costs, track late returns and damage charges, process payments and generate management reports.


## 2. Features

- **Vehicle management:** Manage Economy Cars, SUVs and Luxury Cars.
- **Vehicle availability:** Track whether a vehicle is available or currently rented.
- **Customer management:** Register customers and maintain their rental histories.
- **Vehicle search:** Search available vehicles by category and maximum daily rate.
- **Rental management:** Create rentals, prevent double-booking and record vehicle returns.
- **Rental cost calculation:** Apply the correct pricing rule for each vehicle category.
- **Late-return charges:** Calculate a penalty of 20% of the daily rate for each late day.
- **Damage charges:** Include applicable damage charges in the final bill.
- **Payment processing:** Demonstrate M-Pesa, card and cash payments.
- **Revenue tracking:** Increase revenue only when a payment succeeds.
- **Management reporting:** Display vehicle availability, customer and rental totals, revenue and vehicle category counts.
- **Rental cancellation:** Cancel an active rental and make its vehicle available again. Attempts to cancel a completed or already-cancelled rental are rejected.

## 3. Technologies Used

- Python
- Python Object-Oriented Programming
- Abstract Base Classes (`abc`)
- Git and GitHub
- Visual Studio Code

The project uses Python's standard library and does not require third-party packages.

## 4. Project Structure

```text
RentFlow/
├── main.py
├── vehicle.py
├── customer.py
├── rental.py
├── payment.py
├── rental_system.py
├── README.md
├── docs/
│   └── RentFlow_Class_Diagram.png
└── screenshots/
    ├── main-output.png
    ├── rental-receipt.png
    ├── cancellation.png
    ├── mgmt-report.png
    ├── created-rentals.png
    └── rent-history.png
```

## 5. How to Run the Project

### Prerequisites

Install Python 3 and Git. Open the project folder in Visual Studio Code or another Python-compatible editor.

### Run the program

Open a terminal in the project directory and execute:

```bash
python main.py
```

On some Windows installations, use:

```bash
py main.py
```

The program runs a demonstration of the rental workflow, including vehicle registration, customer registration, vehicle rental, return processing, payment processing, rental histories, management reporting and the rental cancellation bonus feature.

## 6. Sample Data

The demonstration includes at least five vehicles, three customers and three completed rentals.

| Vehicle category | Example vehicle | Daily rate |
|---|---|---:|
| Economy Car | Toyota Axio | KSh 4,000 |
| SUV | Toyota Prado | KSh 8,000 |
| SUV | Nissan X-Trail | KSh 6,500 |
| Luxury Car | Mercedes-Benz E-Class | KSh 15,000 |
| Economy Car | Honda Fit | KSh 3,500 |

The demonstration uses different payment methods to show how payment processing works. It also includes a late return, a damage charge, an attempt to rent an unavailable vehicle and a rental cancellation test.

## 7. Class Responsibilities

- **Vehicle:** Abstract parent class that stores vehicle details, protects availability and defines the rental cost calculation method.
- **EconomyCar, SUV, and LuxuryCar:** Vehicle subclasses that implement their respective pricing rules.
- **Customer:** Stores customer information and maintains rental history.
- **Rental:** Connects a customer to a vehicle and manages rental status, charges, totals and payment status.
- **Payment:** Abstract parent class that defines the payment interface.
- **MpesaPayment, CardPayment, and CashPayment:** Implement different payment methods.
- **CarRentalSystem:** Manages vehicles, customers, rentals, payments, business rules, revenue and management reports.

## 8. Application of the Four OOP Pillars

### Abstraction

Abstraction is demonstrated by the `Vehicle` and `Payment` abstract classes. They define methods that their subclasses must implement without prescribing the specific implementation. For example, `Vehicle` defines `calculate_rental_cost()`, while `Payment` defines `process_payment()`.

### Inheritance

Inheritance is demonstrated by `EconomyCar`, `SUV`, and `LuxuryCar`, which inherit from `Vehicle`. The payment subclasses, `MpesaPayment`, `CardPayment`, and `CashPayment`, inherit from `Payment`. The child classes reuse common attributes and behaviour while implementing their specialised requirements.

### Polymorphism

Polymorphism is demonstrated when `calculate_rental_cost()` produces different prices for economy cars, SUVs, and luxury cars. Similarly, `process_payment()` is implemented differently by M-Pesa, card and cash payments. The system can call these methods through a common interface without needing to implement each type's behaviour in the same way.

### Encapsulation

Encapsulation protects important information from uncontrolled modification. Vehicle availability is stored in the private attribute `__available`, rental payment status in `__paid`, and business revenue in `__revenue`. Methods control state changes, while the `revenue` property provides read-only access to the revenue total.

## 9. Business Rules and Validation

The system enforces important business rules, including:

- Daily rates and applicable payment amounts cannot be negative.
- Customers must have a driving licence and be registered before renting.
- Vehicles must belong to the fleet and be available before they can be rented.
- Rental periods must be greater than zero.
- A vehicle cannot be rented again while unavailable.
- Only active rentals can be completed or cancelled.
- Late fees and damage charges are included in the final rental total.
- Payments can only be processed for completed rentals and cannot be recorded twice.
- Revenue increases only after a successful payment.

Invalid operations raise clear exceptions where applicable.

## 10. Bonus Feature: Rental Cancellation

The project includes rental cancellation as a bonus feature. The `cancel_rental()` methods in `Rental` and `CarRentalSystem` allow an active rental to be cancelled. A successful cancellation changes the rental status to `CANCELLED` and makes the vehicle available again. The system rejects repeated cancellation and cancellation of rentals that are no longer active.

## 11. Class Diagram and Screenshots

The class diagram and screenshots of the running application are included in the project documentation.

- Class diagram: `docs/RentFlow_Class_Diagram.png`
- Main program output: `screenshots/main-output.png`
- Rental receipt: `screenshots/rental-receipt.png`
- Cancellation demonstration: `screenshots/cancellation.png`
- Management report: `screenshots/mgmt-report.png`
- Created rentals: `screenshots/created-rentals.png`
- Rental History: `screenshots/rent-history.png`

## 12. Conclusion

RentFlow demonstrates how Python and Object-Oriented Programming can be used to organise a car rental business workflow. By combining abstraction, inheritance, polymorphism and encapsulation, the system provides a foundation for managing vehicles, customers, rentals, payments and business reporting in a more structured way.
