from abc import ABC,abstractmethod
class add():
    def __init__(self):
        self.a=23
        self.b=3
    @abstractmethod
    def sum(self):
        none
class display(add):
    def sum(self):
        print("sum=",self.a+self.b)
o=display()
o.sum()
