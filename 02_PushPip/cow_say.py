from cowsay import cowsay
from argparse import ArgumentParser

argparser = ArgumentParser(
                    description=
                    """
                    Special module for a python-cowsay module,
                    that helps him be called from the terminal.
                    """
                    )

argparser.add_argument('message', nargs = '?',
                    action = 'store',
                    help = "Cow's message."
                    )

args = argparser.parse_args()
print(cowsay(args.message))