thisdict = {
    "ID": 1,
    "Q": "What colour is an apple?",
    "Ans": "A"
}
x = thisdict["Q"]
y = thisdict["Ans"]
while True:
    d1a = input(x + "\n A) Red. B) Blue. C) Purple. [A/B/C]? : ").upper()
    if d1a == y:
        print(y + " is correct!")
        break
    elif d1a != y:
        print ("that is incorrect!")
        break   
