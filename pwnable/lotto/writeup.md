# Writeup
In this level, the program is randomize 6 bytes, and then we need to guess it.
Brute force may work, but it  will be difficult cause there is 6 bytes, and 45 option for each one.

### Bug
Luckily for us, there is a bug in comparing our guess with the lotto bytes.
```c
// calculate lotto score
int match = 0, j = 0;
for(i=0; i<6; i++){
    for(j=0; j<6; j++){
        if(lotto[i] == submit[j]){
            match++;
		    printf("match is %d", match);
		}
	}
}
```
There isn't any check for duplicate guess.

### Example
If the lotto random bytes values are:
12, 33, 09, 02, 13, 15
It is enough we will guess one of the bytes right and enter it 6 times, for example:
12, 12, 12, 12, 12, 12

*Great Success*
You can just brute force it that way or see the script in solve.py
