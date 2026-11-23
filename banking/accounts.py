import string
import random

class Account:
  
  def __init__(self):
    self.accounts = []
    name = input("Enter your full name: ")
    pin = input("Create your full pin: ")

    listOfNumbers = list(string.digits)
    acc_digits =[]
  
    for _ in range(7):
      digit = random.choice(listOfNumbers)
      acc_digits.append(digit)
    
    acc_number = "".join(acc_digits)
      

      
    
    self.accounts.append({
      "Name": name,
      "Pin": pin,
      "AccountNumber": f"021{acc_number}"
                         })

  


    






