# Writeup
For this level there is a basic vulnerability founded in source code of the 'bet' function

```C
int betting() //Asks user amount to bet
{
 printf("\n\nEnter Bet: $");
 scanf("%d", &bet);
 
 if (bet > cash) //If player tries to bet more money than player has
 {
    printf("\nYou cannot bet more money than you have.");
    printf("\nEnter Bet: ");
    scanf("%d", &bet);
    return bet;
 }
 else return bet;
} // End Function
```
Supposed to be a check if the bet count is negative, but there isn't.
So you can just input a negative number like -10000 and loose in purpose, and be a millionaire.
GG
