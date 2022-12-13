from abc import ABC


class Parent(ABC):
    def __init__(self, networth):
        self.networth = networth

    def declaration(self):
        print('My net worth is', self.networth, 'but implement constraint to avail my net worth')

    @classmethod
    def constraint(cls):
        pass


class Child(Parent):

    def __init__(self, networth):
        self.networth = networth
        super().__init__(networth)

    def inherit(self):
        print('Rs', self.networth, 'inherited')

    def constraint(self):
        print('I am fair enough skilled Dad !')


obj = Child(10)

# obj.inherit(), throws error if abstractclassmethod constraint not implemented
obj.inherit()
