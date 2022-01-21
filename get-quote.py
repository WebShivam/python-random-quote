import random
def primary():
   #print("Keep it logically awesome.")
  with open("quotes.txt", "a") as file:
    file.write("\nAll Things are difficult before they are easy") #adding quotes programmatically
  f = open("quotes.txt", encoding="utf8")
  quotes = f.readlines()
  f.close()

  last=len(quotes)-1
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
