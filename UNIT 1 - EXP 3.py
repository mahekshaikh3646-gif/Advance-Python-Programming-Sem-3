# Strategy Interface
class Payment:
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCard(Payment):
    def pay(self, amount):
        print("Payment of ₹", amount, "done using Credit Card")


class PayPal(Payment):
    def pay(self, amount):
        print("Payment of ₹", amount, "done using PayPal")


class UPI(Payment):
    def pay(self, amount):
        print("Payment of ₹", amount, "done using UPI")


# Context Class
class ShoppingCart:
    def __init__(self):
        self.payment = None

    def setPayment(self, payment):
        self.payment = payment

    def checkout(self, amount):
        self.payment.pay(amount)


# Main Program
cart = ShoppingCart()

print("1. Credit Card")
print("2. PayPal")
print("3. UPI")

choice = int(input("Enter your choice: "))
amount = int(input("Enter amount: "))

if choice == 1:
    cart.setPayment(CreditCard())
elif choice == 2:
    cart.setPayment(PayPal())
elif choice == 3:
    cart.setPayment(UPI())
else:
    print("Invalid Choice")
    exit()

cart.checkout(amount)
