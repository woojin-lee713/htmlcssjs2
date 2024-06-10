class Observable:
    "An observable represents a stream of data over time."
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def emit(self, value):
        for observer in self.observers:
            observer(value)

class ScanOperator:
    "accumulates values over time"
    def __init__(self, accumulator, initial):
        self.accumulator = accumulator
        self.state = initial
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def emit_observer(self, value):
        self.state = self.accumulator(self.state, value)
        for observer in self.observers:
            observer(self.state)

def print_scan_observer(value):
    print(f"Counter is: {value}")

def print2_scan_observer(value):
    print(f"Counter (once again) is: {value}")

if __name__ == "__main__":
    click_observable = Observable()

    # Define the scan operator to accumulate the count
    def increment(acc, value):
        return acc + 1

    counter = ScanOperator(increment, 0)
    # Observable's subscribers are ScanOperator's observers
    click_observable.subscribe(counter.emit_observer)
    # ScanOperator's subscribers are print_scan_observer and print2_scan_observer
    counter.subscribe(print_scan_observer)
    counter.subscribe(print2_scan_observer)

    # Simulate button clicks
    click_observable.emit(1)  # Counter: 1
    click_observable.emit(1)  # Counter: 2
    click_observable.emit(1)  # Counter: 3
