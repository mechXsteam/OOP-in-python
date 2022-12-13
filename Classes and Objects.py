# objectname = classname()

class Dog:
    # class attributes, common to all class instances (objects). Use @classmethod to change the class attribute.
    specie = 'German shepard'

    # methods are the functions defined in a class,
    # 1. magic methods : runs automatically as soon as an instance to a class is created.
    # 2. normal methods: needs to be called explicitly.

    # constructor: special method, constructor can be of two types, default (without any arguments) and parameterized
    # constructor (with arguments provided by the programmer).
    def __init__(self, name, age):
        # instance attributes, specific to a particular class instance (object)
        self.name = name
        self.age = age
        # self.name = name creates an attribute 'name' for the object and assigns it to the 'name' parameter passed as
        # the input.
        # Similar is the case for self.age = age.

    # example of @classmethod
    @classmethod
    def change_specie(cls, specie):
        Dog.specie = specie

    # description : another special method
    def __str__(self):  # __str__() : returns the string representation of the object
        return f'{self.name} is {self.age} years old and it belongs to {self.specie}'

    # normal function
    def speak(self):
        return f'{self.name} says woof!!!'

    # what if we need a function which neither requires object nor class, to create such methods we use @staticmethod.
    @staticmethod
    def utility_function():
        print('some utility function about dogs')


d1 = Dog('miles', 4)  # instantiating

# d1 is known as reference variable

# What if, instead of assigning the object created to a variable, we do this

Dog('tommy', 6)  # instantiating

# will the object be created?

# Answer is yes!, Dog('dog_name','age') creates an object of the class and assigns the address of the object to the
# variable. So the variable just stores the address of the object created. It is known as reference variable.

print(d1)
# Without use of @classmethod decorator, classname must be passed to change the class attribute
Dog.change_specie('Golden Retriever')
print(d1)
Dog.utility_function()

# vars and dir are used to get all the instance attributes of a class object
print(vars(d1))
