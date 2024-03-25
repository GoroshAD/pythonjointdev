import sys
import socket
import cmd
from threading import Thread
import readline
import shlex

def sender(client, sock, commands):
    sock.sendall(commands.encode())
    res = sock.recv(1024).rstrip().decode()
    print(f"\n{res}\n{client.prompt}{readline.get_line_buffer()}", end="", flush=True)


class Cowchat(cmd.Cmd):
    """
    Cow chat client.
    """
    prompt = "=)"
    sock = 0

    def __init__(self, sock):
        self.sock = sock
        return super().__init__()

    def do_who(self, args):
        req = Thread(target = sender, args = (self, self.sock, "who\n"))
        req.start()

    def do_cows(self, args):
        req = Thread(target = sender, args = (self, self.sock, "cows\n"))
        req.start()

    def do_login(self, args):
        req = Thread(target = sender, args = (self, self.sock, f"login {args}\n"))
        req.start()

    def complete_login(self, text, line, begidx, endidx):
        self.sock.sendall("cows\n".encode())
        logins = shlex.split(self.sock.recv(1024).rstrip().decode())[3:]
        return [c for c in logins if c.startswith(text)]

    def do_say(self, args):
        rec, args = shlex.split(args)
        req = Thread(target = sender, args = (self, self.sock, f"say {rec} {args}\n"))
        req.start()

    def complete_say(self, text, line, begidx, endidx):
        self.sock.sendall("who\n".encode())
        logins = shlex.split(self.sock.recv(1024).rstrip().decode())[3:]
        return [c for c in logins if c.startswith(text)]

    def do_yield(self, args):
        req = Thread(target = sender, args = (self, self.sock, f"yield {args}\n"))
        req.start()

    def do_quit(self, args):
        req = Thread(target = sender, args = (self, self.sock, f"quit\n"))
        req.start()

    def do_EOF(self, args):
        return True

    def emptyline(self):
        pass

host = "localhost" if len(sys.argv) < 2 else sys.argv[1]
port = 1338 if len(sys.argv) < 3 else int(sys.argv[2])
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    Cowchat(s).cmdloop()
