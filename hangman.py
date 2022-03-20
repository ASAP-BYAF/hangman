def hangman(word):
    wrong = 0
    stages = [
        "",
        "_______",
        "|",
        "|      |",
        "|      O",
        "|     /|\\",
        "|     / \ ",
        "|",
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hangman")
    used = []
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter : "
        char = input(msg)
        used.append(char)
        if char in rletters:
            used[-1] += "!"
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        print("You already use these words", used)
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("You lose! The answer is {}.".format(word))

word_list = [cat, fight, python, left, center, iron]
indx = random.randint(0, len(wordlist) - 1)
hangman(word_list[indx])