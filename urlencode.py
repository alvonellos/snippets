#Code snippet that safely encodes URLS using the % notation.
# Ex. http://www.stuff.com/image[1].jpg will get
# encoded to something that's web-browser safe. (I hope)

import urllib, sys
while 1:
    try:
        line = sys.stdin.readline()

    except KeyboardInterrupt:
        break

    if not line:
        break

    print urllib.quote(line.strip(), safe=':').strip('\'')