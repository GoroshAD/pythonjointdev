from cowsay import cowsay, Option
from argparse import ArgumentParser

argparser = ArgumentParser(
                    description=
                    """
                    Special module for a python-cowsay module,
                    that helps him be called from the terminal.
                    """
                    )

argparser.add_argument('message', 
                    nargs='?',
                    default="Hello there!",
                    action='store',
                    help="Cow's message."
                    )

argparser.add_argument('-e', '--eyes', 
                       default=Option.eyes,
                       action = 'store',
                       help="Eye-string."
                       )

args = argparser.parse_args()
print(cowsay(args.message, eyes=args.eyes))