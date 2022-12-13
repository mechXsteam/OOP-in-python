class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def speak(self):
        return f'{self.name} says woof!!!'


# we know the fact that custom classes are mutable, therefore we can modify the attributes and methods of the class
# like so,

# modifying attributes, like name
dog = Dog('Tommy', 6)
dog.name = 'Riley'
print(dog.name)


# modifying methods, like speak
def new_speak():
    return f'{dog.name} says hehe!!!'


dog.speak = new_speak()
print(dog.speak)


# Now, this scenario can be dangerous when aimed to develop some intricate software systems for banking sector,
# military sector etc. Therefore, to ensure some amount of safety we can make those vulnerable attributes and methods
# private like so, __attribute(or method)

class New_Dog:

    def __init__(self, name, age):
        # private instance attributes
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'{self.__name} is {self.__age} years old'

    # private method
    def __speak(self):
        return f'{self.__name} says woof!!!'


new_dog = New_Dog('Tommy', 6)

# Now, private variables are not allowed to be accessed from outside the class

# print(new_dog.__name), it creates errors and block further code, hence commented. Uncomment to observe the changes.

# and if we change the name attribute from outside, it won't be reflected.
new_dog.__name = 'something random'
print(new_dog.__name)
print(new_dog)

# But, 'nothing is private in python'. We can still change the value of that private variable from outside the class
# like so,

new_dog._New_Dog__name = 'Whisker'
# print(new_dog.__name)
print(new_dog)


# The name of the private variable changes to _className__attribute(or method), hence in this way private variable still
# can be modified (Hacker!!).

# But why python allows this behaviour ?
# The phrase commonly used is "we're all consenting adults here". By prepending a single underscore (don't expose) or
# double underscore (hide), you're telling the user of your class that you intend the member to be 'private' in some
# way. However, you're trusting everyone else to behave responsibly and respect that, unless they have a compelling
# reason not to (e.g., debuggers and code completion). [stackoverflow]

# Now, the method discussed above is the unethical way of changing the private attributes or methods. Looking into the
# class, get the name of the private variable and modifying it unethically which is allowed to do due to some weired
# python philosophy.

# Let's look at the ethical way of doing the same using two functions-getter and setter. These are two methods defined
# inside the class which allows to access the private variables and modify it values respectively. Since, we are
# allowing the access of private variables via functions, it is in our hand that how the value of the private variables
# are going to be changed.

class Super_Dog:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'{self.__name} is {self.__age} years old'

    def __speak(self):
        return f'{self.__name} says woof!!!'

    # getter
    def getter(self):
        return self.__name, self.__age

    # setter
    def setter(self, new_name, new_age):
        # we can put more validation as per required by the situation
        self.__name = new_name
        self.__age = new_age


super_dog = Super_Dog('Alex', 4)
print(super_dog.getter())
super_dog.setter('jade', 7)
print(super_dog)
