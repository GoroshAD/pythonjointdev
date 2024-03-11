import cmd, shlex
from cowsay import cowsay

class Cowsay(cmd.Cmd):
    """
    Special cowsay module for using cowsay command
    in the command line.
    """
    prompt = "=)"

    def do_EOF(self, args):
        return True

if __name__ == "__main__":
    Cowsay().cmdloop()
