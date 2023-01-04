class MyDescriptor:
    def __init__(self, default_value):
        self.default_value = default_value
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default_value)

    def __set__(self, instance, value):
        self.data[instance] = value

class MyClass:
    my_descriptor = MyDescriptor(0)

obj1 = MyClass()
obj2 = MyClass()

print(obj1.my_descriptor)  # Output: 0
print(obj2.my_descriptor)  # Output: 0

obj1.my_descriptor = 100
print(obj1.my_descriptor)  # Output: 100
print(obj2.my_descriptor)  # Output: 0
