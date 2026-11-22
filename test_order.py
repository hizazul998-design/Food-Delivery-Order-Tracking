
import unittest
from unittest.mock import Mock
from order import Order


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order = Order()
        self.customer = Mock()
        self.kitchen = Mock()

    def test_add_observer(self):
        self.order.add_observer(self.customer)
        self.assertIn(self.customer, self.order.observers)

    def test_remove_observer(self):
        self.order.add_observer(self.customer)
        self.order.remove_observer(self.customer)
        self.assertNotIn(self.customer, self.order.observers)

    def test_notify_all_observers(self):
        self.order.add_observer(self.customer)
        self.order.add_observer(self.kitchen)

        self.order.set_status("Cooking")

        self.customer.update.assert_called_once_with("Cooking")
        self.kitchen.update.assert_called_once_with("Cooking")

    def test_kitchen_not_notified_after_removal(self):
        self.order.add_observer(self.customer)
        self.order.add_observer(self.kitchen)

        self.order.remove_observer(self.kitchen)
        self.order.set_status("Delivered")

        self.customer.update.assert_called_once_with("Delivered")
        self.kitchen.update.assert_not_called()

    def test_status_change(self):
        self.order.set_status("Cooking")
        self.assertEqual(self.order.status, "Cooking")


if __name__ == "__main__":
    unittest.main()
