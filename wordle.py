# GRACE DONAHER
# WORDLE CODE (FOR FUN!)

# ASK FOR THE CORRECT WORD
correctWord = input("What is the correct word: ")
# INITIALIZES RESULT AS EMPTY STRING
result = ""

# CHECKS TO SEE IF THE WORD IS RIGHT, RUNS AGAIN IF NOT
while result != "🟩🟩🟩🟩🟩":
    # RESETS RESULT AS EMPTY STRING
    result = ""
    # ASK FOR THE USER'S GUESS
    userGuess = input("What is the user's guess: ")
    # FOR LOOP TO ITERATE THROUGH THE CHARACTERS IN THE WORDS
    for i in range(5):
        # IF STATEMENTS FOR SIMILARITIES
        # RETURN GREEN IF LETTER IN THE RIGHT SPOT
        if userGuess[i] == correctWord[i]:
            result = result + "🟩"
        # RETURN YELLOW IF LETTER IN THE WORD BUT WRONG SPOT
        elif userGuess[i] in correctWord:
            result = result + "🟨"
        # RETURN WHITE IF LETTER NOWHERE IN WORD
        else:
            result = result + "⬜"
    print(result)