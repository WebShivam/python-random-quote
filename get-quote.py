#file = open(quotes.txt, encoding="utf8")
import random
def primary():
   #print("Keep it logically awesome.")

  f = open("quotes.txt", encoding="utf8")
  quotes = f.readlines()
  f.close()

  last = 19
  rnd = random.randint(0, last)
  print(quotes[last])

if __name__== "__main__":
  primary()
