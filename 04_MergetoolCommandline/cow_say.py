import cmd, shlex
from cowsay import list_cows, make_bubble

class Cowsay(cmd.Cmd):
    """
    Special cowsay module for using cowsay command
    in the command line.
    """
    prompt = "=)"
    

    def do_list_cows(self, args):
        """
        Show list of available cows.
        Usage: list_cows
        """
        print(list_cows())

    def do_make_bubble(self, args):
        """
        Print a bubble with text.
        Usage: make_bubble text TEXT
        """
        args = shlex.split(args)
        print(dict(zip(args[::2], args[1::2])))
        print(make_bubble(**dict(zip(args[::2], args[1::2]))))

    def do_EOF(self, args):
        """
        End the commands with EOF.
        Usage: EOF
        """
        return True

if __name__ == "__main__":
    Cowsay().cmdloop()
