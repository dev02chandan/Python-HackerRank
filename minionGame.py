def minion_game(string):
    Kevin, Stuart = 0, 0

    vowels = ["A", "E", "I", "O", "U"]

    for i in range(len(string)):
        for j in range(1, len(string) + 1):
            substring = string[i:j]
            if substring:
                if substring[0] in vowels:
                    Kevin += 1
                else:
                    Stuart += 1

    if Kevin > Stuart:
        print("Kevin ", Kevin)
    elif Kevin < Stuart:
        print("Stuart ", Stuart)

    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
