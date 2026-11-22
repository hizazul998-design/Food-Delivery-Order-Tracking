
from order import Order
from observers import SMSNotifier, KitchenNotifier

# Create order
order = Order()

# Create observers
customer = SMSNotifier("Rahim")
kitchen = KitchenNotifier()

# Add observers
order.add_observer(customer)
order.add_observer(kitchen)

# Change order status
order.set_status("Cooking")

order.set_status("Out for delivery")

# Remove kitchen observer
order.remove_observer(kitchen)

# Final status
order.set_status("Delivered")
