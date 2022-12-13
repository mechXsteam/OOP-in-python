# OOP's Cheatsheet

**What is it?** 

- Way of writing code apart from procedural programming.
- Way of modelling real-life entities.
# Classes and objects

**Class is the blueprint**, and the **object is an instance** of that blueprint.

Analogies

- Car is a class, and the TATA harrier is an object to that car class.
- A class is like a form or a questionnaire. An instance is like a form that has been filled out with information.

Classes 

- built-in
- user-defined

```python
class ClassName:
	# constructor
	def __init__(self):
		pass
	# methods
	def method(self):
		pass

obj = ClassName()
```
What is the **self**?

Self is the reference of the instance of the class created.

Functions defined in a class are known as **methods.**

**Constructor?**

- __init__() is a special method called a ‘constructor’ that sets the class's initial state by assigning values to the object properties. Unlike other functions, it doesn’t require to be called explicitly. It is called as soon as an instance of the class is created.
- Python creates a default constructor for every class. But if we create our own constructor, it does not create a default constructor.
- Special methods are also known as dunder or magic methods.

Attributes specific to an object are **instance attributes**, such as name, age, etc., of an object.

Attributes common to all objects are **class attributes**, such as country, planet etc., of an object.

Creating an object is known as **instantiating**.

Custom objects are mutable and can be altered dynamically.

Classes do not occupy memory. When instances of classes are created, then only memory is consumed.
# Encapsulation

Encapsulation in Python is **wrapping the data and methods** within a single unit. 

A class implementation is an example of encapsulation as it binds all the data members (instance variables) and methods into a single unit.

It allows us to make the attributes and methods of the class private, i.e. inaccessible to the outside World.

In the class diagram, private variables are denoted with a (-) prefix, and public variables are denoted with a (+) variable.

# Inheritance

Inheritance allows a child class to inherit attributes and methods from the parent class. A child class can have its own properties along with the properties of the parent class. So, the child class (derived class) is a subset of the parent class (base class). Inheritance improves code reusability and readability.

What can be inherited?

- Parent class constructor
- Parent class non-private methods and attributes

Types of Inheritance

1. Single
2. Multiple
3. Multilevel
4. Hierarchical
5. Hybrid

### Some Useful Methods

1. isinstance() → This function is used to check whether an object is an instance of a particular class. It returns a boolean value of True if the object is an instance and, otherwise, False.
    
    bool = isInstance(obj,class)
    
2. issubclass() → This function is used to check whether a class is derived from a parent class. It returns a boolean value True if the two classes share a parent-child relationship and, otherwise, False.
    
    bool = issubclass(child class,parent class)
    

# Abstraction

An abstract class contains at least one abstract method.

A method declared but contained no implementation is known as an abstract method.

Abstract classes are used to set some constraints for child classes during inheritance.

We can’t create an object of abstract classes.