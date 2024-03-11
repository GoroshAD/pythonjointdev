import cmd, shlex
from cowsay import list_cows

class Cowsay(cmd.Cmd):
    """
    Special cowsay module for using cowsay command
    in the command line.
    """
    prompt = "=)"
    

    def do_list_cows(self, args):
        """
        Show list of available cows.
        """
        print(list_cows())

    def do_EOF(self, args):
        """
        End the commands with EOF.
        """
        return True

if __name__ == "__main__":
    Cowsay().cmdloop()
