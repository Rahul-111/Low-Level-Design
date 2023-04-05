from abc import ABC, abstractmethod


# Observable Interface
class Observable(ABC):
    def add(self, obj):
        pass

    def remove(self, obj):
        pass

    def notify(self):
        pass

    def setData(self, data):
        pass


# Observer Interface
class Observer(ABC):
    def update(self, obj):
        pass


# implement Observable interface/ abstract class

class WeatherStation(Observable):
    def __init__(self):
        self.Observers = []
        self.temperature = 0

    # add an observer
    def add(self, obj):
        self.Observers.append(obj)

    def remove(self, obj):
        self.remove(obj)

    def notify(self):
        for observer in self.Observers:
            # has a relationship pass observable object
            observer.update(self)

    # Whenever temperature gets update call all the observer
    def setData(self, new_temperature):
        self.temperature = new_temperature
        self.notify()

    def getData(self):
        return self.temperature


# implement Observer interface/ abstract class

class LEDDisplayObserver(Observer):
    def __init__(self):
        print("LEDScreen init")

    # receive observable object and render the data
    def update(self, obj):
        print(f"Render the new temperature which is {obj.getData()}")


w1 = WeatherStation()

# create the observer
Led1 = LEDDisplayObserver()
Led2 = LEDDisplayObserver()
Led3 = LEDDisplayObserver()

# add observer for observable
w1.add(Led1)
w1.add(Led2)
w1.add(Led3)

w1.setData(10)
# w1.setData(25)