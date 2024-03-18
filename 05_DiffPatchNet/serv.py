import asyncio
from cowsay import list_cows
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
                        if commands[1] not in list_cows():
                            writer.write("Error: use 'cows' to see existing login name.\n".encode())
                            continue
                        if commands[1] in users.keys():
                            writer.write("Error: this login is already in use, choose another one.\n".encode())
                            continue
                        my_id = commands[1]
                        users[my_id] = my_queue
                        print(f"{me} my id is {my_id}")
                        writer.write(f"Your id now is {my_id}.\n".encode())
                    case "who":
                        writer.write(("Online users are:\n" + " ".join(users.keys()) + "\n").encode())
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
