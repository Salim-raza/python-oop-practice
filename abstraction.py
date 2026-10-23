from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
    
class BkashPayment(Payment):
    def pay(self, amount):
        print(f"Bkash payment: {amount} taka")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Card payment: {amount} taka")
        
bkash = BkashPayment()
card= CardPayment()

bkash.pay(500)
card.pay(100)