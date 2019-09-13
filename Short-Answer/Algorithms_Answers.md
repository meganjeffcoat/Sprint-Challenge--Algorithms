#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n^1) - n is growing linearly in this snippet. n grows at a rate of n^3 while a is growing at a rate of n^2
n is the make or break in this snippet. As n grows so does the runtime

b) O(n^2) - There are 2 loops in this snippet. Each loop is an O(n), they get multiplied together to get the O(n^2) runtime. n is being checked twice.

c) O(n) - For more specificity this would actually be O(n - 1), the reason for this is because it is a recursive function.
It is running linearly and subtracted by 1 each time the recursive call is made.

## Exercise II

- `n` is the number of stories in the building
- we need to find `f` which would be the "break point", egg breaks at this height or higher
- need to check which floors the egg breaks when dropped
- find the middle index `n/2` and drop the egg, the bottom will always be 0, the top is n and the middle is `top/2`
- if the egg breaks we know we are too high or at the most bottom floor that will break the egg
- once a check is done on the first median index, find the new median index again, this time we go to the floor between the current floor and the most bottom floor
- if the egg didn't break we know we are too low, so we go to the median floor between the floor we are currently on which is now the `most_bottom` and the previous floor we were on
- repeat the pattern of bisecting the remaing floors above or below the current floor
- this will do a binary search and return the minimum floor that an egg can be dropped and broken

Runtime:

The best case would be: O(1), the building would be one floor
On agerage: O(log(n)), the building will need to be bisected `m` times `log(n) - m*log(2)`
