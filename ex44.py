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


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.Override()
son.Override()

dad.altered()
son.altered()