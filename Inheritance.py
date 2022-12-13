# Single Inheritance

# parent class
class Phone:
    def __init__(self, brand):
        print("Inside phone constructor")
        self.brand = brand
        self.__private = None

    def func(self):
        return 'Hello World from Parent class'


# Smartphone inherits from phone class
class SmartPhone(Phone):
    def __init__(self, name, os, ram, price, brand):
        print("Inside SmartPhone constructor")
        super().__init__(brand)
        self.name = name
        self.os = os
        self.ram = ram
        self.price = price
        print(f'name- {self.brand} {self.name}, price- {self.price}, ram- {self.ram}, os- {self.os}')

    # method overriding
    def func(self):
        return 'Hello World from the Child Class'


s1 = SmartPhone("GalaxyX90", "Android", '8GB', 48000, 'Samsung')
# we can access the parent class attributes, but not the private ones
print(s1.brand)
print(s1.func())


# What is that super() keyword ?

class Parent:
    def __init__(self):
        self.attr1 = 50
        self.attr2 = 60


class Child1(Parent):
    def __init__(self):
        super().__init__()
        self.attr3 = 40


obj1 = Child1()
# print(obj.attr1) -> error
print(obj1.attr1)


# This happens due to method overriding. Method overriding is an ability of any object-oriented programming language
# that allows a child class to execute implementation of its own method against a method already provided by its parent
# class.Since __init__() is a special method declared both in parent and child class therefore this method is overridden
# in the child's class. Therefore, to access parent class attributes and methods declared in the constructor, we use
# super() keyword.

class Child2(Parent):
    def __init__(self):
        super().__init__()
        # or, Parent.__init__(self)
        self.attr3 = 40


obj2 = Child2()
print(obj2.attr1)


# Multiple Inheritance

class parent1:  # first parent class
    def func(self):
        print("Hello Parent1")


class parent2:  # second parent class

    def func(self):
        print("Hello Parent2")


class parent3:  # third parent class
    def func(self):
        print("Hello Parent3")


class child(parent1, parent2, parent3):  # child class
    def func3(self):  # we include the parent classes
        print("Hello Child")


child1 = child()
child1.func()

# If two parents have the same named methods, the child class performs the method of the first parent in order of
# reference. Languages like JAVA suffers ambiguity in such type of problem (known as diamond problem), but python don't
# because it follows mro.
# order of reference -> Child class > parent1 > parent2 > parent3 (multiple resolution order, mro)

# Based on the above concepts we can have, multilevel, hierarchical and hybrid inheritance.

# some important functions

bool1 = isinstance(obj1, Child1)
print(bool1)

bool2 = issubclass(SmartPhone, Phone)
print(bool2)
