#include <stdio.h>

int ret_four()
{
	return 4;
}

int main()
{
		int x = 0;
		if(x=ret_four()>3)
		{
			printf("pass the if condition\n");
		}
		printf("%d\n", x);
		return 0;
}
