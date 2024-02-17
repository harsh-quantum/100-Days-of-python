from replit import db
import os
import time
import datetime 
def Add():
  tweet = input("Enter your tweet: > ")
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}"
  db[key] = tweet
  time.sleep(1)
  os.system("clear")
  
def View():

  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(0.3)
    counter += 1
    if(counter%10==0):
      carryOn = input("Next 10?: ")
      if(carryOn.lower()=="no"):
        break
  time.sleep(1)
  os.system("clear")

while(True):
    print("""======  Menu   ========
    
          1: Add 
          2: View
          3: Exit """)
    user = input(" Enter the option (1/2/3): >")
    if user == "1":
      Add()
    elif user == "2":
    
      View()
    elif user == "3":
      break
    else:
      print(" Wrong Input")
      time.sleep(1)
      os.system("clear")