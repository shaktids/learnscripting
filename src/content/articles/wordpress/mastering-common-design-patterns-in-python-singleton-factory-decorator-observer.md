---
title: "Mastering Common Design Patterns in Python: Singleton, Factory, Decorator, Observer"
description: "In the realm of software engineering, mastering design patterns is akin to wielding a versatile toolkit that empowers developers to solve complex problems…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2024-04-28T17:35:05Z
legacy: true
wpId: 5129
---

In the realm of software engineering, mastering design patterns is akin to wielding a versatile toolkit that empowers developers to solve complex problems efficiently. Python, with its simplicity and flexibility, provides an ideal environment for implementing these patterns seamlessly. In this blog post, we'll delve into four common design patterns in Python: Singleton, Factory, Decorator, and Observer.

### Singleton Pattern

The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. This pattern is useful when exactly one object is needed to coordinate actions across the system.

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Output: True
```

### Factory Pattern

The Factory pattern defines an interface for creating objects but allows subclasses to alter the type of objects that will be created. It provides a centralized place for creating objects, making the code more modular and maintainable.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Truck(Vehicle):
    def drive(self):
        return "Driving a truck"

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'truck':
            return Truck()
        else:
            raise ValueError("Invalid vehicle type")

# Usage
car = VehicleFactory.create_vehicle('car')
print(car.drive())  # Output: Driving a car
```

### Decorator Pattern

The Decorator pattern allows behavior to be added to individual objects dynamically, without affecting the behavior of other objects from the same class. It's useful for extending the functionality of objects without subclassing.

```python
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

# Usage
print(greet('John'))  # Output: HELLO, JOHN!
```

### Observer Pattern

The Observer pattern defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically. It's useful for implementing distributed event handling systems.

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class ConcreteSubject(Subject):
    def __init__(self, state=None):
        super().__init__()
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self.notify()

class Observer:
    def update(self):
        pass

class ConcreteObserver(Observer):
    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        print(f"Observer: Subject's state has changed to {self._subject.state}")

# Usage
subject = ConcreteSubject()
observer1 = ConcreteObserver(subject)
observer2 = ConcreteObserver(subject)

subject.state = "New State"  # Output: Observer: Subject's state has changed to New State
```

### Conclusion

Understanding and applying design patterns in Python can significantly enhance code quality, maintainability, and scalability. The Singleton, Factory, Decorator, and Observer patterns presented in this blog post represent just a glimpse into the world of design patterns. By incorporating these patterns into your Python projects, you'll be equipped to tackle complex software design challenges with elegance and efficiency. Keep exploring, experimenting, and mastering the art of software design patterns in Python. Happy coding!
