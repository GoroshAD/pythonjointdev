import asyncio
from cowsay import list_cows
import shlex

users = {}

async def chat(reader, writer):
    me = "{}:{}".format(*writer.get_extra_info('peername'))

    my_id = None
    my_queue  = asyncio.Queue()

    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(clients[me].get())

    while not reader.at_eof():
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())
                commands = shlex.split(q.result().decode())
                match commands[0]:
                    case "login":
                        if commands[1] not in list_cows():
                            writer.write("Error: use 'cows' to see existing login name.")
                        if commands[1] in users.keys():
                            writer.write("Error: this login exists, use another login name.")
                        my_id = commands[1]
                        users[my_id] = my_queue

            elif q is receive:
                receive = asyncio.create_task(users[my_id].get())
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
