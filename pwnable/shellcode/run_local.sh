#!/bin/sh
nasm -f elf64 ./hello.asm
ld -o ./hello ./hello.o  
./hello
echo "\n$?"
rm ./hello.o
