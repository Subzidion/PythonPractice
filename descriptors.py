class DataDescriptor:
    def __init__(self, value=0):
        self.value = value

    def __get__(self, instance, cls):
        print("I can run __get__ specific code")
        return self.value

    def __set__(self, instance, value):
        print("I can run __set__ specific code")
        self.value = value + 10

    def __delete__(self, instance):
        print("I can run __delete__ specific code")
        print("I do nothing.")

class MyClass:
    attr = DataDescriptor()
