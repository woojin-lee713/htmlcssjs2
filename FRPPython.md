### Functional Reactive Programming (FRP) in Pure Python

Let's build a simple FRP example from scratch using pure Python. We'll create a reactive counter without any external libraries.

### Step 1: Define Observable

An observable represents a stream of data over time.

```python
class Observable:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def emit(self, value):
        for observer in self.observers:
            observer(value)
```

### Step 2: Define Observer

An observer listens to changes in the observable and reacts accordingly.

```python
def print_observer(value):
    print(f"Counter: {value}")
```

### Step 3: Implement Scan Operator

The `scan` operator accumulates values over time, similar to the `reduce` function.

```python
class ScanOperator:
    def __init__(self, accumulator, initial):
        self.accumulator = accumulator
        self.state = initial
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def emit(self, value):
        self.state = self.accumulator(self.state, value)
        for observer in self.observers:
            observer(self.state)
```

### Step 4: Create Counter Example

Combine these components to create a reactive counter.

```python
# Define the observable for button clicks
click_observable = Observable()

# Define the scan operator to accumulate the count
def increment(acc, value):
    return acc + 1

counter = ScanOperator(increment, 0)
click_observable.subscribe(counter.emit)
counter.subscribe(print_observer)

# Simulate button clicks
click_observable.emit(1)  # Counter: 1
click_observable.emit(1)  # Counter: 2
click_observable.emit(1)  # Counter: 3
```

### Explanation:

1. **Observable**: Manages a list of observers and emits values to them.
2. **Observer**: Reacts to values emitted by the observable.
3. **Scan Operator**: Accumulates values over time and emits the accumulated result.
4. **Counter Example**: Combines these components to create a reactive counter that increments and prints its value when simulated button clicks are emitted.

This example demonstrates the basics of functional reactive programming using pure Python, with observables and observers handling state changes over time.