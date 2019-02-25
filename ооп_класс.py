#import ооп_класс_для_импорта
#import weakref

class A:
    attr1 = 42
    attr2 = 'string'
    x = int(input('input number:'))
    def summa(x, attr1):
        return x + attr1

test = A()

print(A.attr1)
print(A.attr2)
print(test.attr1, test.attr2)
print("________")

A.attr1 = 234
test.attr2 = 'hueta'
print(A.attr1, test.attr2)
print(A.attr2, test.attr2)


