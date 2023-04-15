import socket
import re

ADDRESS= ("pwnable.kr", 9007)
COIN_WEIGHT = 10
FAKE_COIN = 9

def game_loop(s: socket.socket):
	line = s.recv(100).decode()
	data = ""
	# Ugly as fuck.
	n = line.split()[0][line.find("=")+1:]
	c = line[line.find("=",line.find("=")+1)+1:len(line)-1]
	print(f"N: {n}, C: {c} ")
	fake_coin = game_iteration(s, 0, int(n), int(c))
	print(f"fake coin index {fake_coin}")
	while "Correct!" not in data:
		s.send(fake_coin.encode())
		data = s.recv(1024).decode()
	print(data)



def game_iteration(s, low, high, c):
	guess = low + int((high - low + 1) / 2)
	guess_line = " ".join([str(num) for num in range(low, guess)]) + "\n"

	if c == 0:
		return guess_line

	# print(f"guess {c}: {guess_line}")
	s.send(guess_line.encode())
	#weight = int(s.recv(200).decode()[:-1])
	weight = int(s.recv(200).decode())

	expected_weight = (guess - low) * COIN_WEIGHT
	# print(f"original coins weight: {expected_weight}")
	# print(f"got weight: {weight}")

	if weight == FAKE_COIN:
		return guess_line

	if (len(guess_line.split()) == 1):
		# import ipdb;ipdb.set_trace()
		pass

	# Didn't guess fake coin.
	if expected_weight == weight:
		return  game_iteration(s, guess, high, c-1)

	# Guess faked coin.
	return  game_iteration(s, low, guess, c-1)


def main():
	s = socket.socket()
	s.connect(ADDRESS)	
	data = s.recv(2048).decode()
	for i in range(100):
		print(f"Entering game {i}")
		game_loop(s)

	flag = s.recv(1024).decode()
	print(f"Flag is {flag}")
	s.close()


if __name__ == '__main__':
	main()
