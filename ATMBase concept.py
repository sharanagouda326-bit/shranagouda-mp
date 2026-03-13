
from abc import ABC,abstractmethod

class ATMBase(ABC):

   @abstractmethod
   def check_balance(self):
      pass

   @abstractmethod
   def deposit(self):
      pass

   @abstractmethod
   def withdraw(self):
      pass

#ATM class
class ATM(ATMBase):

   def __init__(self):
      self.__balance = 1000
      self.transaction = []


   def check_balance(self):
         print("your balance", self.__balance)

   def deposit(self):
         amount = int(input("enter amount to deposit: "))
         self.__balance = self.__balance + amount
         self.transaction.append("deposited"+ str(amount))

         print("deposit successful")
   def withdraw(self):
         amount = int(input("enter amount to withdraw: ")) 
         if amount <=self.__balance:
            self.__balance = self.__balance - amount
            self.transaction.append("withdraw" + str(amount))
            print("please collect your money")
         else:
            print("insufficient balance")
   def showtransaction(self):
         print("transaction history")
         for t in self.transaction:
            print(t)

atm = ATM()

while True:
   print("\n===== ATM MENU =====")
   print("1. check balance")
   print("2.deposit")
   print("3.withdraw")
   print("4.transaction")
   print("5.exit")


   choice = int(input("enter your choice:"))
   if choice == 1:
      atm.check_balance()
   elif choice == 2:
      atm.deposit()
   elif choice == 3:
      atm.withdraw()
   elif choice == 4:
      atm.showtransaction()
   elif choice == 5:
      print("thank you for using ATM")
      break

   else:
      print("invalid option")
   
