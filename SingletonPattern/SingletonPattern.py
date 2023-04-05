class Singleton:
    singleton_instance = None

    def __init__(self):
        if Singleton.singleton_instance is None:
            Singleton.singleton_instance = self
        else:
            raise Exception("This class is a singleton class !")

    # @classmethod
    # def getSingleton(cls):
    #     if not cls.singleton_instance:
    #         cls.singleton_instance = Singleton()
    #         return cls.singleton_instance
    #     else:
    #         return cls.singleton_instance

    @staticmethod
    def getInstance():
        if Singleton.singleton_instance is None:
            Singleton.singleton_instance = Singleton()
        return Singleton.singleton_instance


# How to stop this step
# s2 = Singleton()
#
# print(id(Singleton.singleton_instance))
# t = Singleton.getInstance()
# print(id(t))
# t2 = Singleton.getInstance()
# print(id(t2))


# s3 = Singleton()
# print(id(Singleton.singleton_instance))
# ---OUTPUT-----
# Singleton Object Instantiated
# 4306452096
# 4306452096
# Both Address are same ==> no new object is getting created


class SingletonExample:
    class_variable = None

    def __init__(self):
        if SingletonExample.class_variable is None:
            SingletonExample.class_variable = self
        else:
            # if already initialised
            raise Exception("This class is Singleton")

    @classmethod
    def getInstance(cls):
        # object is not initialise only then initialise
        if cls.class_variable is None:
            cls.class_variable = SingletonExample()
        # if already initialise then no need to perform any action simple return the previous initialisation
        return cls.class_variable


s1 = SingletonExample()

c1 = SingletonExample.getInstance()
c2 = SingletonExample.getInstance()

s4 = SingletonExample()

print(id(c1))
print(id(c2))
