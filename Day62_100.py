from replit import db
import os
import time
import datetime
import getpass

def add():

  x = input(" Wnter your thoughts: > ")
  timestamp = datetime.datetime.now()
  db[timestamp] = x
  
def view():
  m = input("1. Search for exact date \n2. Last entry \n")

  
  keys = list(db.keys())
  if m == "1":
    date_input = input("Enter date (YYYY-MM-DD): ")
    
    match = [item for item in keys if item.startswith(date_input)]
    # print(match)  
    if len(match) == 0:
      print(" No entry found for that date.")
    else:  
      for key in match :
        print(f"{key} {db[key]}")
        print()
  else:
    for key in reversed(keys):
      print(f"{key} {db[key]}")
      print()
      time.sleep(0.3)
      next = input("Next or exit? > ")
      if(next.lower()[0]=="e"):
        break

print(" Welcome the diary \n")
password = getpass.getpass("Enter your password:  > ")

if password == "password":
  print(" Welcome ") 
  while(True):

    print("1. Add \n2. View \n3. Exit  ")
    user = input(">: ")
    if user == "1":
      add()
    elif user == "2":
      view()  
    else:
      break
else:
  print(" Wrong Password")