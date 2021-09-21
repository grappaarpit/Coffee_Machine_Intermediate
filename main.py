from menu import MENU
from menu import resources
import os
os.system('clear')
power = True
enough = True
notenough=0
# function report
def report():
  for i in resources:
    print(f"{i}: {resources[i]}")

# function OFF machine   
def off():
  print("The machine is switching off, goodbye")
  return False



def make_coffee(drink):
  money = 0
  quantity= enough(drink)
  if(quantity==1):
    return
  money = funds(drink)
  if(money==0):
    return
  deduct(drink)
  print(f"Enjoy your {drink} ☕️ ☕️ ☕️ ☕️")

    

# check function
def enough(drink):
  global notenough
  for k in MENU:
    if k ==drink:
      if(MENU[k]["ingredients"]["water"]>resources["Water"]):
        print("Sorry there is not enough water")
        notenough = 1
      if(MENU[k]["ingredients"]["milk"]>resources["Milk"]):
        print("Sorry there is not enough milk")
        notenough = 1
      if(MENU[k]["ingredients"]["coffee"]>resources["Coffee"]):
        print("Sorry there is not enough coffee")
        notenough = 1
  return notenough
        
#process coins
def funds(drink):
  print("Put in the money now: ")
  quarters = float(input("How many quarters: ")) 
  dimes = float(input("How many dimes: ")) 
  nickles = float(input("How many nickles: ")) 
  pennies = float(input("How many pennies: ")) 
  total = (0.25*quarters)+(0.1*dimes)+(0.05*nickles)+(0.01*pennies)
  for l in MENU:
    if l ==drink:
      if(MENU[l]["cost"]>total):
        print("Sorry that's not enough money. Money refunded.")
        return 0
      elif (MENU[l]["cost"]<=total):
        resources["Money"] += MENU[l]["cost"]
        change = total - MENU[l]["cost"]
        if change > 0:
          print(f"Here is {change:.2f} dollars in change")
        return 1
        
#deliver coffee
def deduct(drink):
  for n in MENU:
    if n ==drink:
      resources["Water"]-=MENU[n]["ingredients"]["water"]
      resources["Milk"]-=MENU[n]["ingredients"]["milk"]
      resources["Coffee"]-=MENU[n]["ingredients"]["coffee"]

        
         


  







# while not OFF MACHINE
while(power):

  # ask user
  notenough=0
  drink = input("​What would you like? (espresso/latte/cappuccino): ")

  if drink =="report":
    report()
  
  elif drink =="off":
    power=off()
  
  elif drink == "espresso" or drink == "latte" or drink == "cappuccino" :
    make_coffee(drink)









        

    