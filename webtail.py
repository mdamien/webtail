#!/usr/bin/env python

import asyncio
import websockets
import sys
import sh
import functools

@asyncio.coroutine
def tail_it(websocket, uri, filepath):
    try:
        for line in sh.tail('-f',filepath,_iter=True):
            yield from websocket.send(line)
    except Exception as e:
        print(e)

if len(sys.argv) != 3:
    print("Usage: python webtail.py FILEPATH PORT")
else:
    filepath, port = sys.argv[1], int(sys.argv[2])
    print("Tail of %s on port %d" % (filepath, port))
    tail_it_partial = functools.partial(tail_it, filepath=filepath)
    start_server = websockets.serve(tail_it_partial, 'localhost', port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
