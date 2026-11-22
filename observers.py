
class SMSNotifier:
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def update(self, status):
        print(
            f"SMS to {self.customer_name}: "
            f"your order is now {status}"
        )


class KitchenNotifier:
    def update(self, status):
        print(f"Kitchen screen: {status}")
