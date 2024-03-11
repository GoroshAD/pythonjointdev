import cmd, shlex
from cowsay import list_cows, make_bubble, cowsay, cowthink

class Cowsay(cmd.Cmd):
    """
    Special cowsay module for using cowsay command
    in the command line.
    """
    prompt = "=)"
    text = "text"
    cow = list_cows()
    eyes = ["OO", "oO", "Oo", "oo", "..", "0O", "xx", "--", "TT", "==", "++", "$$", "::", "()", "~~"]
    tongue = [" U", "U ", "# ", " #", "| ", " |", " /", "/ ", "\ "]
    attributes = ["message", "cow", "eyes", "tongue"]

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
        print(make_bubble(**dict(zip(args[::2], args[1::2]))))

    def do_cowsay(self, args):
        """
        Print a cow with its message.
        Usage: cowsay message MESSAGE [cow COW] [eyes EYES] [tongue TONGUE]
        """
        args = shlex.split(args)
        print(cowsay(**dict(zip(args[::2], args[1::2]))))

    def do_cowthink(self, args):
        """
        Print a cow with its message in a bubble.
        Usage: cowthink message MESSAGE [cow COW] [eyes EYES] [tongue TONGUE]
        """
        args = shlex.split(args)
        print(cowthink(**dict(zip(args[::2], args[1::2]))))

    def complete_make_bubble(self, text, line, begidx, endidx):
        if self.text.startswith(text):
            return [self.text]

    def complete_cowsay(self, text, line, begidx, endidx):
        tmp = shlex.split(line)[-2 if text else -1]
        match tmp:
            case "cow":
                return [i for i in self.cow if i.startswith(text)]
            case "eyes":
                return [i for i in self.eyes if i.startswith(text)]
            case "tongue":
                return [i for i in self.tongue if i.startswith(text)]
            case _:
                return [i for i in self.attributes if i.startswith(text)]

    def do_EOF(self, args):
        """
        End the commands with EOF.
        Usage: EOF
        """
        return True

if __name__ == "__main__":
    Cowsay().cmdloop()
