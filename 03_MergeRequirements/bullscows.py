from random import choice
from argparse import ArgumentParser
from urllib.request import urlopen
from cowsay import cowsay, list_cows, read_dot_cow
from io import StringIO

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
    secret = choice(words)
    attempts_at_all = 0
    guess = ""
    while guess != secret:
        guess = ask("Введите слово: ", words)
        attempts_at_all += 1
        b, c = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", b, c)
    return attempts_at_all

def ask(prompt: str, valid: list[str]=None) -> str:
    tmp_cow = read_dot_cow(StringIO("""$the_cow = <<EOC;
   $thoughts
    $thoughts
         ______________
       /                \\
       |                |
       |   \__    __/   |
       |    []\  /[]    |
       \__            __/
          \    /\    /
           \        /
           |/\/\/\/\|

           |/\/\/\/\|
           \________/

EOC"""))
    print(cowsay(prompt, cowfile=tmp_cow))
    guess = input()
    if valid is not None:
        while guess not in valid:
            print(cowsay(prompt, cowfile=tmp_cow))
            guess = input()
    return guess

def inform(format_string: str, bulls: int, cows: int) -> None:
    tmp_cow = choice(list_cows())
    print(cowsay(format_string.format(bulls, cows), cow=tmp_cow))

parser = ArgumentParser(description = 
                        """
                        Module-game bulls and cows.
                        """
                        )
parser.add_argument('dictionary',
                    help="Dictionary with the words, that are used for this game."
                    )
parser.add_argument('length',
                    nargs='?',
                    default=5,
                    type=int,
                    help="The length of the words in the game."
                    )
args = parser.parse_args()
words = []
try:
    with open(args.dictionary) as file:
        words = file.read().split()
except:
    with urlopen(args.dictionary) as file:
        words = file.read().decode('utf-8').split()
words = list(filter(lambda x: len(x) == args.length, words))
print(gameplay(ask, inform, words))

