from SuperClass import SuperClass1
from SuperClass2 import SuperClass2

class ChildClass(SuperClass1, SuperClass2):
    def child_method(slef): 
        print("child_method")


c = ChildClass()
c.method_super1()
c.method_super2()
print(isinstance(c,SuperClass2))