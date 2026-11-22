class Order:
    def __init__(self):
        self.status = "Placed"
        self.observers = []

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def set_status(self, new_status):
        self.status = new_status
        print(f"Order is now: {new_status}")

        for observer in self.observers.copy():
            observer.update(new_status)
