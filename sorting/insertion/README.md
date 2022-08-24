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

## Step-Through
- First of all, here's our input array:

`[8, 4, 23, 42, 16, 15]`

- Let's use our pseudo-code write some Python code and step through the problem, one iteration at a time...

```Python
values = [8, 4, 23, 42, 16, 15]

def insertion_sort(arr):
  for i, num in enumerate(arr):
    # print(i)
    j = i - 1
    # print(i, j)
    # temp = nums[i]
    while j >= 0 and num < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
      
    arr[j+1] = num

print(values)
insertion_sort(values)
print(values)
```
