webtail
=======

Tail a file in you browser

#### Install #####

You need python 3.4 or python 3.3 with the asyncio library.

    mkvirtualenv webtail
    pip install sh websockets
    python webtail.py YOUR_FILE 9000

and serve the index.html file

To test it, you can use generate.py to get a nice "updating periodically" file.
