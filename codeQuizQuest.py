myvar = 0
QUESTIONS = [
    ("What is 9+10?  [A]19.  [B]21.  [C]7.", "A"),
    ("What colour is an apple?  [A]Purple.  [B]Red.  [C]Blue.", "B"),
    ("What day is Halloween on?  [A]Oct31st.  [B]Fri13th.  [C]Sept22nd.", "A"),
    ("What day is Christmas on?  [A]Feb14th.  [B]Dec25th.  [C]May20th.", "B"),
    ("How many minutes in an hour?  [A]60.  [B]22.  [C]35.", "A"),
    ("Which one of these birds cant fly?  [A]Chicken.  [B]Tui.  [C]Kakapo.", "C")
]
#Correct Answers: A, B, A, B, A, C.
QUESTIONSTWO = [
    ("What is 9x7?  [A]19.  [B]63.  [C]7.", "B"),
    ("How many letters are in the english alphabet?  [A]25.  [B]32.  [C]26.", "C"),
    ("30 Days of September, April June and?  [A]November.  [B]July.  [C]December.", "A"),
    ("What day is only on a leap year?  [A]Feb29th.  [B]May32nd.  [C]Jun31st.", "B"),
    ("Whats heavier; 1kg of steel, or 1kg of feathers?  [A]Feathers.  [B]Steel.  [C]They're both the same.", "C"),
    ("What are the three primary colours of light?  [A]Red, Green, Blue.  [B]Cyan, Magenta, Yellow.  [C]Red, Yellow, Blue.", "A"),
    ("How many elements are in the periodic table?  [A]112.  [B]118.  [C]147.", "B"),
    ("How many native flightless birds does New Zealand have?  [A]17.  [B]16.  [C]21.", "B")
]
#Correct Answers: B, C, A, B, C, A, B, B.
for question, correct_answer in QUESTIONS:
    answer = input(f"{question} [A/B/C] ").upper()
    if answer == correct_answer:
        print("Correct!")
        myvar = myvar + 1
        print("SCORE:")
        print(myvar)
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        print("SCORE:")
        print(myvar)
    if myvar == 4:
        QUESTIONS.extend(QUESTIONSTWO)
