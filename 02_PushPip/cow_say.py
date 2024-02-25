from cowsay import cowsay
from argparse import ArgumentParser

argparser = ArgumentParser(
                    description=
                    """
                    Special module for a python-cowsay module,
                    that helps him be called from the terminal.
                    """
                    )

argparser.add_argument('message', 
                    default="Hello there!",
                    nargs='?',
                    action='store',
                    help="Cow's message."
                    )

argparser.add_argument('-e', '--eyes', 
                        default='oo',
                        nargs='?',
                        action = 'store',
                        help="Eye-string."
                        )

argparser.add_argument('-f', '--file', 
                       default="www",
                       nargs='?',
                       action = 'store',
                       help="Custom cow-file."
                       )

args = argparser.parse_args()
print(cowsay(args.message, eyes=args.eyes, cow=args.file))
