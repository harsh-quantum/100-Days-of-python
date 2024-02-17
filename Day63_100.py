import random
import test as hang

listOfWords = ["DownTRon"]


wordChosen = random.choice(listOfWords)
count = 0
guess_list=[]
list_input =[]

for i in range(len(wordChosen)):
  guess_list.append("_")

while True:
  temp_chosen = wordChosen
  print()
  p = input("Choose a letter: ").lower()

  if p in list_input:
    print(" This alphabet is already guessed")
    print(f"You have {count} lives left")
    guess_word = hang.hangmanlife(guess_list)
    print(guess_word)
  else:
    list_input.append(p)
    if p in temp_chosen.lower():
      print("Correct!")

      for pos in range(len(wordChosen)):
        if p == temp_chosen[pos].lower():
          guess_list[pos] = wordChosen[pos]
      guess_word = hang.hangmanlife(guess_list)
      print(guess_word)
      if "_" not in guess_list:
        print(f"You won with {count} lives left.")

        ask = input(" Do you want to play more (Y/N) ?")
        if ask == 'Y':
            True
        else:
            break
    else:
      print("Nope, not in there.")
      print(type(count))
      hang.HANGMANPICS(count)
      count += 1
#       print(f"You have {count} lives left")
      if count == 7:
        print(" HANGMANNNNNN")
        print("You lost!")
        break