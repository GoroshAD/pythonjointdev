from cowsay import cowsay, list_cows
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

argparser.add_argument('-l', '--list', 
                       default=False,
                       nargs='?',
                       action = 'store',
                       help="Show a list of cows. (True/False)"
                       )

args = argparser.parse_args()
if args.list:
    print(list_cows())
else:
    print(cowsay(args.message, eyes=args.eyes, cow=args.file))
