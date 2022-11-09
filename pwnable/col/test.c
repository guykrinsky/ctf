#include <stdio.h>
// test integer overflow

int main(int argc, char** argv)
{
	printf("start of  program\n");
	int a = argv[1][1];
	printf("argv: %x\n", a);
}

