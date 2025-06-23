#suppose app accepts multiple payemnet methods
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("not implemented")
    
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit card")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class Cash(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Cash")

def cheackout(payment_method, amount):
    payment_method.pay(amount)

credit = CreditCard()
upi = UPI()
cash = Cash()

cheackout(credit, 200)
cheackout(upi, 200)
cheackout(cash, 200)