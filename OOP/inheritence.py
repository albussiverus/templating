class Class1:
    def __init__(self):
        print("Constructor")
    def method_1(self):
        print("Helloo from method_1")

    def method_2(self):
        print("Helloo from method_2")


class Class2(Class1):

    def __init__(self):
        print("from class2")
    def method_class2(self):
        print("Helloo from method_class2")



my_obj = Class2()

my_obj.method_1()
my_obj.method_2()
my_obj.method_class2()
