# Singleton class

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class MyClass(object):
    pass

my1 = MyClass()
my2 = MyClass()

print my1
print my2

