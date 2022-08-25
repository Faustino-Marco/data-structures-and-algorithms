# Insertion Sort
Wondering how to code an <em>Insertion Sort<em> algorithm? Look no further! This blog post is going to walk you through all the steps you'll take to get from pseudo-code to working-code!

## What's Insertion Sort?

An insertion sort method or function will take an array of integers as input and sort them, in this case, in ascending order.

## Pseudo Code
Here's the pseudo-code we're starting with:
```Python
 InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

## Python Code
First of all, here's our input array:

`[8, 4, 23, 42, 16, 15]`

- Let's use our pseudo-code to write some Python code and step through the problem, one iteration at a time...

```Python
values = [8, 4, 23, 42, 16, 15]

def insertion_sort(arr):
  for i, num in enumerate(arr):
    j = i - 1
    while j >= 0 and num < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = num

print(values)
insertion_sort(values)
print(values)
```

## Step-Through
Each pass through the array in our function `insertion_sort(values)` evaluates the indices and values at each index in the input array (values).

We set the variable `j` equal to the index - 1. This way, we can compare each value to the value that came before it.

If the current value at the index in question is less than the value at index `j`, or index - 1, then the greater of the two replaces the current value. 

## Result
The result is a sorted array, in ascending order. 

`[4, 8, 15, 16, 23, 42]`