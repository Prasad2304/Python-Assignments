#hierarchical inheritance

class parent:
    def parent_property(self):
        print("parent has a house")

class child1(parent):
    def child1_property(self):
        print("child1 has a car")

class child2(parent):
    def child2_property(self):
        print("child2 has a bike")

child1 = child1()
child1.parent_property()
child1.child1_property()

child2 = child2()
child2.parent_property()
child2.child2_property()


