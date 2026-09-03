#multiple inheritance

class Father:
    def father_property(self):
        print("Father has a car")


class Mother:
    def mother_property(self):
        print("Mother has a house")


class Child(Father, Mother):
    def child_property(self):
        print("Child has a laptop")


child = Child()

child.father_property()
child.mother_property()
child.child_property()