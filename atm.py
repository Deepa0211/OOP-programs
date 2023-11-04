# ATM apps

class Atm():
    # pin 
    # balance
    pin = None
    balance = 0
    
    # card activation
    def activate_card(self):
        print("Hi!! Welcome to SBI ATM")
        self.pin = input("Create a 4 digit pin ")
        
        print("Congratulations!! Your card is activated")
        
    # check balance
    def check_balance(self):
        temp = input("Enter your 4-digit pin ")
        if temp == self.pin:
            print("Your current balance is", self.balance)
        else:
            print("Invalid pin number")
                  
    # deposit
    def deposit(self):
        temp = input("Enter your 4-digit pin ")
        if temp == self.pin:
            amount = int(input("Enter the amount "))
            self.balance = self.balance + amount
            print("Amount has been deposited successfully")
        else:
            print("Invalid pin number")
            
    # withdraw
    def withdraw(self):
        temp = input("Enter your 4-digit pin ")
        if temp == self.pin:
            amount = int(input("Enter the amount "))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Amount has been withdrawn successfully")
            else:
                print("Amount entered is more than balance")
        else:
            print("Invalid pin number")
        
    