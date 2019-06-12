class Parent(object):
    def implicit(self):
        print("PARENT implict ()")
    
    def Override(self):
        print("PARENT override ()")

    def altered(self):
        print("PARENT altered ()")


class Child(Parent):
    def Override(self):
        print("Child Override()")
    
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child,self).altered()
        print("CHILD, AFTER PARENT altered()")

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class A(Other):
    def __init__(self):
        self.other = Other()
    def implicit(self):
        print("A override()")

    def altered(self):
        print("A, BEFORT altered()")
        self.other.altered()
        print("A, AFTER altered()")       


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.Override()
son.Override()

dad.altered()
son.altered()


a = A()

a.implicit()
a.override()
a.altered()