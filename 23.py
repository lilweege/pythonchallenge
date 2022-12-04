s = "va gur snpr bs jung?"
for c in s:
    if ord('a') <= ord(c) <= ord('z'):
        print(chr(((ord(c) - ord('a') + 13) % 26) + ord('a')), end="")
    else:
        print(c, end="")

import this
