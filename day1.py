"""
https://docs.google.com/presentation/d/1AUCGB4bzeGyqqVWru6Ukm90oksyd8cUdy-47lpiZoBc/edit?usp=sharing
"""
#Lecture example 1: 
ex_text = "Hi how are ya?"
ex_int = 2
ex_float = 2.0
bool_ex = False

#For example
for x in [ex_text, ex_int, ex_float, bool_ex]: 
    print(x)

#While Example
print("While example: \n")
x = 0
while x <= 20:
    print(x)
    x+=1 
print(x)
# ^ Pay attention to that second print, see what happens without it...


#Example Code for assignment
import random
list_ex = random.sample(range(10), 5) 
#10 is the biggest a number can be 
#5 == len(list_ex)

#Do some things with lists!: 
#Find the smallest number in list_ex

#Find the biggest number in list_ex


#Class Example
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"


# Usage
account = BankAccount("Alice", balance=100.0)
account.deposit(50.0)
account.withdraw(30.0)
print(account.get_balance())  # 120.0
print(account)                # BankAccount(owner='Alice', balance=120.00)

#Your turn! 
class yourClass: 
    def __init__(self, variable : list = []):
        self.variable = random.sample(range(10), 5)
"""
    def sortLow():

    def sortHigh(): 

    def findLow():

    def findHigh(): 
"""

