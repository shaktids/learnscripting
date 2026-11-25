---
title: "Groovy Inheritance and Polymorphism: A Comprehensive Guide"
description: "Introduction In object oriented programming (OOP), inheritance and polymorphism are fundamental concepts that help organize and extend code efficiently…"
lang: other
categories: ["Groovy"]
author: "Shakti Das"
pubDate: 2023-10-07T03:35:16Z
legacy: true
wpId: 4134
---

Introduction

In object-oriented programming (OOP), inheritance and polymorphism are fundamental concepts that help organize and extend code efficiently. Groovy, a dynamic and versatile language for the Java Virtual Machine (JVM), provides robust support for these concepts. In this blog post, we'll explore Groovy's inheritance and polymorphism features, how to use them effectively, and why they are essential in building flexible and maintainable code.

## Inheritance in Groovy

Inheritance is a mechanism that allows you to create a new class (the child or subclass) based on an existing class (the parent or superclass). The child class inherits properties and methods from the parent class while having the flexibility to add new features or override existing ones.

### Defining a Superclass

In Groovy, you define a superclass by creating a class with its properties and methods. For example, let's define a `Vehicle` superclass:

```groovy
class Vehicle {
    String make
    String model

    Vehicle(String make, String model) {
        this.make = make
        this.model = model
    }

    void start() {
        println("$make $model is starting.")
    }
}
```

### Creating a Subclass

A subclass in Groovy is created by defining a new class and using the `extends` keyword to specify the superclass. In this example, we'll create a `Car` subclass that extends `Vehicle`:

```groovy
class Car extends Vehicle {
    int year

    Car(String make, String model, int year) {
        super(make, model)
        this.year = year
    }

    @Override
    void start() {
        println("$year $make $model car is starting.")
    }

    void drive() {
        println("$year $make $model car is driving.")
    }
}
```

### Inheriting and Overriding

The `Car` subclass inherits the `make` and `model` properties and the `start` method from the `Vehicle` superclass. It also overrides the `start` method to provide a customized implementation. Additionally, it adds a `drive` method that is specific to the `Car` class.

### Creating and Using Objects

You can create objects of both the superclass and the subclass:

```groovy
def myCar = new Car("Toyota", "Camry", 2023)
myCar.start() // Output: 2023 Toyota Camry car is starting.
myCar.drive() // Output: 2023 Toyota Camry car is driving.
```

## Polymorphism in Groovy

Polymorphism is a concept that allows objects of different classes to be treated as objects of a common superclass. In Groovy, polymorphism is achieved through method overriding and method overloading.

### Method Overriding

Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. In the `Car` example, we override the `start` method to customize the behavior:

```groovy
@Overridescarcar
void start() {
    println("$year $make $model car is starting.")
}
```

### Polymorphic Behavior

Polymorphism allows you to use a superclass reference to refer to a subclass object. This enables you to write more generic code that can work with multiple types of objects.

```groovy
def myVehicle = new Car("Ford", "Focus", 2022)
myVehicle.start() // Output: 2022 Ford Focus car is starting.
```

Here, `myVehicle` is of type `Vehicle`, but it references a `Car` object. The overridden `start` method in the `Car` class is invoked, demonstrating polymorphic behavior.

## Conclusion

Inheritance and polymorphism are powerful concepts in Groovy that enable you to create organized, maintainable, and flexible code. Inheritance allows you to build class hierarchies and reuse code efficiently, while polymorphism enables objects of different classes to work together seamlessly.

By understanding and leveraging these concepts, you can write code that is easier to maintain and extend, making Groovy an excellent choice for developing scalable and robust applications on the JVM. Groovy's support for inheritance and polymorphism, combined with its dynamic nature, offers developers a powerful and expressive programming experience.
