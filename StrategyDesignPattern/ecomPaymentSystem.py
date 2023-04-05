# For our example, we will try to implement a simple Shopping Cart where 
# we have two payment strategies - 
# using Credit Card 
# or using PayPal. 
# First of all we will create the interface for our strategy pattern example, 
# in our case to pay the amount passed as argument
# https://www.digitalocean.com/community/tutorials/strategy-design-pattern-in-java-example-tutorial


# abstract class provide basic generic trends 
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def make_payment():
        print("Amount Deducted")

class CreditCardStrategy(PaymentStrategy):
    def __init__(self, card_no, cvv, otp) -> None:
        self.card_no = card_no
        self.cvv = cvv
        self.otp = otp

    @staticmethod
    def make_payment(amount):
        print(f"{amount} Deducted via Credit Card")


class UPIStrategy(PaymentStrategy):

    def __init__(self, upi_id , pin) -> None:
        self.upi_id = upi_id
        self.pin = pin 

    @staticmethod
    def make_payment(amount):
        print(f"{amount} Deducted via UPI")


# ShoppingCart ---has a --> Paymentmethos - is a --> CreditCart / UPI 

class item:
    def __init__(self, id, price, qty) -> None:
        self.id = id 
        self.price = price
        self.qty = qty

    def getPrice(self):
        return self.price * self.qty


class ShoppingCart:
    
    def __init__(self) -> None:
        self.itemList = []
        self.amount = 0
        print("You can add item to Bag")

    def addItem(self, item):
        self.itemList.append(item)
        self.amount += item.price

    def removeItem(self, item):
        for product in self.itemList:
            if product.id == item.id:
                self.itemList.remove(item)
                self.amount -= item.price

    def generateBill(self):
        print("You Bill ....\n")
        for item in self.itemList:
            print(f'{item.id}\t\t{item.price}\t\t{item.qty}')

        print(f'Amount to be paid : {self.amount}')


    def checkOut(self, paymentalgo):
        paymentalgo.make_payment(self.amount)


cart = ShoppingCart()
cart.addItem(item(1, 99, 1))
cart.addItem(item(2, 299, 1))
cart.addItem(item(3, 999, 2))

print(f"Total Amount to be paid : {cart.amount}")
cart.generateBill()

cart.checkOut(CreditCardStrategy('1231 1231 2312', '009', 123456))

cart.checkOut(UPIStrategy('mobile@upi', 'pin'))



