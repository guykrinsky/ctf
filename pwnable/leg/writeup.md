# Writeup #
## About The Level
This challenge is about inserting the right value as input.
It is hard to debug this program cause it runs only on arm architecture.
When I needed to debug things on this challenge I used on of the [online arm simulators](https://cpulator.01xz.net/?sys=arm)

## Solution
So we have two files
* my_leg.c - The C code of the program
* my_leg.asm - The gdb dump output of the program (with addresses in him).

### key1
pc - holds the next instruction to be executed (in this case is the next next command cause we got the value of pc after out instruction is running).
key1 value = 0x00008ce4

### key2
key2 was the most confusing one cause of the transition to thumb arm. Transition below:
``` asm
	add	r6, pc, $1\n
	bx	r6\n
```

but It is the same idea as key1, except that now every instruction is two bytes.
key2 = 0x00008d0c

### key3
holds the value of the return address.
key3 = 0x00008d80

### Final Solution
```python
key1 + key2 + key3
```
