import asyncio
from cowsay import list_cows, cowsay
import shlex

users = {}

async def chat(reader, writer):
    me = "{}:{}".format(*writer.get_extra_info('peername'))
    print(me)

    my_id = None
    my_queue  = asyncio.Queue()

    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(my_queue.get())

    while not reader.at_eof():
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())
                commands = shlex.split(q.result().decode())
                match commands[0]:
                    case "login":
                        if len(commands) != 2:
                            writer.write("Invalid arguments.\n".encode())
                            continue
                        if commands[1] not in list_cows():
                            writer.write("Error: use 'cows' to see existing login name.\n".encode())
                            continue
                        if commands[1] in users.keys():
                            writer.write("Error: this login is already in use, choose another one.\n".encode())
                            continue
                        my_id = commands[1]
                        users[my_id] = my_queue
                        print(f"{me}: my id is {my_id}")
                        writer.write(f"Your id now is {my_id}.\n".encode())

                    case "who":
                        if len(commands) != 1:
                            writer.write("Invalid arguments.\n".encode())
                            continue
                        print(f"{me}: using who command")
                        writer.write(("Online users are:\n" + " ".join(users.keys()) + "\n").encode())

                    case "cows":
                        if len(commands) != 1:
                            writer.write("Invalid arguments.\n".encode())
                            continue
                        print(f"{me}: using cows command")
                        writer.write(("Available logins are:\n" + " ".join(list(set(list_cows()) \
                                - set(users.keys()))) + "\n").encode())

                    case "say":
                        if my_id is None:
                            print(f"{me}: trying to use say command without login")
                            writer.write(("You have no rights here, please login.\n").encode())
                            continue
                        if len(commands) != 3:
                            writer.write("Invalid arguments.\n".encode())
                            continue
                        if commands[1] not in users.keys():
                            writer.write("There is no user with this name here.\n".encode())
                            continue
                        print(f"{me}: saying smth to {commands[1]}")
                        await users[commands[1]].put(f"\n{cowsay(commands[2], cow=my_id)}\n")

                    case "yield":
                        if my_id is None:
                            print(f"{me}: trying to use yield command without login")
                            writer.write(("You have no rights here, please login.\n").encode())
                            continue
                        if len(commands) != 2:
                            writer.write("Invalid arguments.\n".encode())
                            continue
                        print(f"{me}: yielding smth")
                        for out in users.values():
                            if out is not users[my_id]:
                                await out.put(f"\n{cowsay(commands[1], cow=my_id)}\n")

                    case "quit":
                        if len(commands) != 1:
                            writer.write(("Well, this is incorrect usage of the command, but okay...\n").encode())
                        print(f"{me}: logs out")
                        writer.write(("You are logged out now.\n").encode())
                        del user[my_id]
                        my_id = None

                    case _:
                        continue
                                
            elif q is receive:
                receive = asyncio.create_task(my_queue.get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()
    send.cancel()
    receive.cancel()
    print(my_id, "DONE")
    del users[my_id]
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1338)
    async with server:
        await server.serve_forever()

asyncio.run(main())
