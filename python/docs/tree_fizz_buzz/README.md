# Tree Fizz Buzz
<!-- Short summary or background information -->
Write a function called fizz buzz tree
- Arguments: k-ary tree
- Return: new k-ary tree

## Challenge
<!-- Description of the challenge -->
Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

- If the value is divisible by 3, - replace the value with “Fizz”
- If the value is divisible by 5, - replace the value with “Buzz”
- If the value is divisible by 3 and 5, - replace the value with “FizzBuzz”
- If the value is not divisible by 3 or - 5, simply turn the number into a - String.

## Whiteboard
(missing pseudo code)
![tree-fizz-buzz-whiteboard](tree-fizz-buzz.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
### Space
O(N) - Storing as many nodes's values as there are nodes in the tree
### Time
O(N) - Hitting each node and operating on it once

## API
<!-- Description of each method publicly available to your Stack and Queue-->