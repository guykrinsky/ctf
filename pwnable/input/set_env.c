#include <stdlib.h>
#include <stdio.h> 

#define ENV_KEY "\xde\xad\xbe\xef"
// #define ENV_KEY "hello"
#define ENV_VALUE "\xca\xfe\xba\xbe"

int main()
{
		setenv(ENV_KEY, ENV_VALUE, 1);
		// printf("value at setting environments  script: %x %x %x %x\n", a[0], a[1], a[2], a[3]);
//		if(a != NULL)
//			printf("hello key: %x %x %x %x\n", a[0], a[1], a[2], a[3]);
//
//		a = getenv(ENV_KEY);
//		if(a != NULL)
//			printf("dead beef key: %x %x %x %x\n", a[0], a[1], a[2], a[3]);
//		else
//			printf("Couldn't find beef key\n");
//
		execve("xargs --null -a argv ./input 0<stdin 2<stderr");
		
}

