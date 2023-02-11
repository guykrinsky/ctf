"""
This level is separated to some stages.
Every stage is independent.
"""
import os

#-------------------------------- First stage - argv.

# Fill argv with garbage.
argv = "a"*99
argv = list(argv)
# Adding null termintero
argv = list("\x00".join(argv))

i = (ord("A")-1)*2
argv.pop(i)
argv[i+1] = "\x20\x0a\x0d"

#-------------------------------- second stage - stdin/err.
with open("stdin", "wb") as tmp:
    tmp.write(b"\x00\n\x00\xFF")

with open("stderr", "wb") as tmp:
    tmp.write(b"\x00\n\x02\xFF")


#-------------------------------- second stage - stdin/err.

# os.system("./set_env")
# ENV_KEY = b"hello"
# ENV_KEY  = b"\xde\xad\xbe\xef"

ENV_KEY = b"\xef\xbe\xad\xde"
ENV_VALUE = b"\xca\xfe\xba\xbe"
os.environb[ENV_KEY] = ENV_VALUE


ENV_KEY = b"hello"
ENV_VALUE = b"\xca\xfe\xba\xbe"
os.environb[ENV_KEY] = ENV_VALUE

os.system("/bin/bash")
#os.system("./set_env")
#os.system("xargs --null -a argv ./input 0<stdin 2<stderr");
