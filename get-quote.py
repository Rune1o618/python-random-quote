import random #This module generates random "numbers"


def primary(): #Because its not C or C++
 # print("Keep it logically awesome.")

  f = open("quotes.txt") #Opens text file and puts it in a variable f
  quotes = f.readlines() #in variable quotes readlines function
  f.close()              #format.close
                         #quotes is an array, so we are calling the first
                         #element of that array
  last = 13  # Since our array has 13 elements we declare it in a last variable
  rnd = random.randint(0,13) #random function imported from random to genetare randint "random integer from 0 - 13"

  print(quotes[rnd])          #print quotes

if __name__== "__main__":
  primary()

