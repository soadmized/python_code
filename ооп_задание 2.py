class MyMeta(type):
    __instances = list()

    def __call__(cls, *args, **kwargs):
        instance = super(MyMeta, cls).__call__(*args, **kwargs)
        cls.__instances.append(instance)

        return instance

# Python3
class MyClass(object, metaclass=MyMeta):
    pass


print(MyClass.__instances)
a = MyClass()
print(MyClass.__instances)
b = MyClass()
c = MyClass()
print(MyClass.__instances)
