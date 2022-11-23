from abc import ABC, abstractmethod

class TestABCClass(ABC):

    @abstractmethod
    def m1(self, a1):
        pass

class TestClass(TestABCClass):

    def m1(self):
        print("FROM TestClass M1")
    def m2(self,):
        print('FROM TestClass M2')


a = TestClass()
a.m1()