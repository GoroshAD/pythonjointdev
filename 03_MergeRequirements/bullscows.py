def bullscows(guess: str, secret: str) -> (int, int):
    bulls, cows = 0, 0
    were_arr = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bulls += 1
        if guess[i] in secret and guess[i] not in were_arr:
            cows += 1
        were_arr.append(guess[i])
    return (bulls, cows)

