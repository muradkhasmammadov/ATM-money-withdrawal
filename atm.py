# -*- coding: utf-8 -*-
"""ATM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18yvEGP_C-f9u2DqbdeKoqcwvmeQF6eoG
"""

class Card:

      def __init__(self, card_number, card_type, pin,):
        self.card_number = card_number
        self.card_type = card_type
        self.pin = pin
      
      def pin_code(self):
        return self.pin

      def checkCardStatus(self):
        return self.card_type


card = Card(4169531232145612, 'debit', 2512)



class ATM:

    def __init__(self, withdrawal, balance):
        self.withdrawal = withdrawal
        self.balance = balance

    def balance_(self):
        print('Your balance now is: ', self.balance)


    def withdrawal_(self):
      code = int(input('Enter PIN code: '))
      if code == card.pin_code():
        withdrawal = int(input("How much money you want to take out: "))
        if self.balance >= withdrawal and acc.Account_Type() == card.checkCardStatus():
          self.balance = self.balance - withdrawal
          print('Request is successful! \nYour balance now is: ', self.balance)
        elif self.balance > withdrawal and acc.Account_Type() != card.checkCardStatus():
          self.balance = self.balance - withdrawal - (withdrawal * 0.015)
          print('Request is successful! \nYour balance now is: ', self.balance)
        else:
          print('You dont have enough money in your balance.')
      else:
          print('Incorrect PIN')

atm = ATM(0, 2000)

class Customer:

      def __init__(self, customer_name, customer_surname, customer_phonenum, customer_address):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.customer_phonenum = customer_phonenum
        self.customer_address = customer_address

      def customer_data(self):
        print('Customer Name: ', self.customer_name)
        print('Customer Surname: ', self.customer_surname)
        print('Customer Phone Number: ', self.customer_phonenum) 
        print('Customer Address: ', self.customer_address)

customer = Customer('Thomas', 'Muller', 37256281291, 'Lubja 1b/4, Tartu, Estonia' )



class Account:

  def __init__(self, balance, account_type):
    self.balance = balance
    self.account_type = account_type

  def Account_Type(self):
    return self.account_type

  def Check_Balance(self):
    return self.balance

acc = Account(2000, 'premium')



def main():
    menu_options = [1, 2, 3, 4]
    while True:
        print("\nSelect an option: \n")
        print("1. Show balance")
        print("2. Withdraw money")
        print("3. Customer Data")
        print("4. Cancel")
        value = int(input("Select a service from menu: "))
        if value == 1:
            atm.balance_()
        elif value == 2:
            atm.withdrawal_()
        elif value == 3:
            customer.customer_data()
        elif value == 4:
            break
        elif value not in menu_options:
            print("Choose a number between 1-3 as an option. ")
            main()
main()