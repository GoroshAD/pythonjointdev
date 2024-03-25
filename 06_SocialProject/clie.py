import sys
import socket
import cmd

class Cowchat(cmd.Cmd):
    sock = 0

    def __init__(self, sock):
        self.sock = sock
        return super().__init__()

    def do_EOF(self):
        return True

    def emptyline(self):
        pass

host = "localhost" if len(sys.argv) < 2 else sys.argv[1]
port = 1337 if len(sys.argv) < 3 else int(sys.argv[2])
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    Cowchat(s).cmdloop()
