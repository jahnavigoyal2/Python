 # suppose order need time stamp when its placed 
from datetime import datetime

class Order:
    def __init__(self, order_id, placed_at):
        self.order_id = order_id
        self.placed_at = placed_at  # datetime object

    def display(self):
        print(f"Order ID: {self.order_id} | Placed at: {self.placed_at}")

    @classmethod
    def create_now(cls, order_id):   #clean way to create orders with current time
        return cls(order_id, datetime.now())

    @classmethod
    def from_string(cls, order_id, date_str): #covert date string into date time object
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        return cls(order_id, dt)


order1 = Order.create_now("A1")
order1.display()

order2 = Order.from_string("A2", "2025-06-23 12:15:00")
order2.display()