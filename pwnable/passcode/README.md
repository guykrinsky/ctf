## Writeup
### First achievement
in this level passcode1 is uninitialized and it's getting it's starting value from the stack.
We can put's what ever value we want into the stuck by our input in welcome function. By this we can set the value of passcode1.
### Second achievement
In the source code there is a mistake that the value of passcode1 is passed to scanf instead of it's address.
### Final solution
By the two achievement we can change the data in what ever address we want.
I changed the flush section in the got table, and when calling to flush, you're actually calling to 'system cat flag'.
