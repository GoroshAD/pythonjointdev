from random import choice

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

def gameplay(ask: callable, inform: callable, words:list[str]) -> int:
    secret = random.choice(words)
    attempts_at_all = 0
    attempt = ""
    while attempt != secret:
        attempt = ask("Введите слово: ", words)
        attempts_at_all += 1
        inform("Быки: {}, Коровы: {}", b, c)
    return attempts_at_all

def ask(prompt: str, valid: list[str]=None) -> str:
    attempt = input(prompt)
    if valid is not None:
        while attempt not in valid:
            attempt = input(prompt)
    return attempt

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))
