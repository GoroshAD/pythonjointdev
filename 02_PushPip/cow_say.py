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
                       default="default",
                       nargs='?',
                       action = 'store',
                       help="Custom cow-file."
                       )

argparser.add_argument('-l', '--list', 
                       nargs='?',
                       action = 'store',
                       help="Show a list of cows. (True/False)"
                       )

argparser.add_argument('-n', '--none', 
                       nargs='?',
                       action = 'store',
                       help="Disable text wrapping."
                       )

argparser.add_argument('-T', '--tongue', 
                       default='  ',
                       nargs='?',
                       action = 'store',
                       help="Tongue-string."
                       )

argparser.add_argument('-W', '--width', 
                       default=40,
                       nargs='?',
                       action = 'store',
                       help="Text width."
                       )

presets = argparser.add_argument_group("presets").add_mutually_exclusive_group()
list_of_stages = ["Borg mode", "dead", "greedy", "paranoia", "stoned", "tired", "wired", "youthful"]
for i in list_of_stages:
    if i == "Borg mode":
        presets.add_argument('-b', 
                     action = 'store_true',
                     help="Borg mode"
                     )
    else:
        presets.add_argument(f'-{i[0]}', 
                        action = 'store_true',
                        help=i
                        )

args = argparser.parse_args()
preset = ''.join(i for i in "bdgpstwy" if getattr(args, i))
if args.list:
    print(list_cows())
else:
    print(cowsay(args.message, eyes=args.eyes, cow=args.file, wrap_text=args.none, 
                 tongue=args.tongue, width=args.width, preset=preset))
