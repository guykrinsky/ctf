#!/bin/sh
nasm -f bin ./hello.asm
cat hello | nc pwnable.kr 9026
