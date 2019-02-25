import weakref


class MyMeta(type):
    def __init__(self, *args, **kwargs):
        self.__instances = {}
        super(MyMeta, self).__init__(*args, **kwargs)

    def get_instances(self):
        return list(self.__instances.values())

    def delete(self, id_instance):
        del self.__instances[id_instance]

    def __call__(self, *args, **kwargs):
        instance = super(MyMeta, self).__call__(*args, **kwargs)
        self.__instances[id(instance)] = weakref.proxy(instance)
        return instance

class MyClass(object, metaclass=MyMeta):
    pass

for obj in MyClass.get_instances:
    print(obj)
