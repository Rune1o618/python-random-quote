def primary(): #Because its not C or C++
 # print("Keep it logically awesome.")

  f = open("quotes.txt") #Opens text file and puts it in a variable f
  quotes = f.readlines() #in variable quotes readlines function
  f.close()              #format.close
                         #quotes is an array, so we are calling the first
                         #element of that array

  print(quotes[0])          #print quotes the 0th element of the arrayx

if __name__== "__main__":
  primary()

