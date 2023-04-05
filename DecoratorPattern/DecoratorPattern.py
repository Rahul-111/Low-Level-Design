from abc import ABC, abstractmethod


# abstract class
class BasePizza(ABC):

    @abstractmethod
    def cost(self):
        pass


# child class of BasePizza
class Margherita(BasePizza):

    def __init__(self):
        print("Initialise Margherita Pizza")

    def cost(self):
        return 100


# child class of BasePizza
class VegiDelight(BasePizza):

    def __init__(self):
        print("Initialise VegiDelight Pizza")

    def cost(self):
        return 200


# abstract class for topping
class ToppingDecorator(BasePizza):
    # it has both the relationship {has-a and is-a relationship } with base pizza class

    def cost(self):
        pass


class ExtraChees(ToppingDecorator):
    # it has both the relationship {has-a and is-a relationship } with base pizza class
    def __init__(self, basePizza):
        self.basePizza = basePizza

    def cost(self):
        return self.basePizza.cost() + 10


class Mushroom(ToppingDecorator):
    # it has both the relationship {has-a and is-a relationship } with base pizza class
    def __init__(self, basePizza):
        self.basePizza = basePizza

    def cost(self):
        return self.basePizza.cost() + 20


# Margherita with extra chees
pizza_1 = Mushroom(ExtraChees(Margherita()))

print(f'Cost of Pizza : {pizza_1.cost()}')
