
SC = 0
while True:
    d1a = input("What colour is an apple?: \n A) Red. B) Blue. C) Purple. [A/B/C]? : ").upper()
    if d1a == "A":
        print("A is correct!")
        SC = SC + 1
        print (SC)
        break
    elif d1a != "A":
        print("That is incorrect!")
        print (SC)
        break
  
        
        