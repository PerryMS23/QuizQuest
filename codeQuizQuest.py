tally = 0
while True:
    d1a = input("What colour is an apple?: \n A) Red. B) Blue. C) Purple. [A/B/C]? : ").upper()
    
    if d1a == "A":
        print("A is correct!")
        tally = tally + 1
        print (tally)
        break
    elif d1a != "A":
        print("That is incorrect!")
        tally = tally
        break
   
    