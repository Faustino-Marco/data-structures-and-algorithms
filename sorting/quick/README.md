# Blog Notes: Quick Sort

## Quick! Let's Quick-Sort a List!

## Pseudo-Code
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

## Python-Code

### Input
Here's our input list:
`[8,4,23,42,16,15]`

### Python


## Stepthrough and Graphics
Essentially, this type of sorting is similar to merge sort, in that it sort (lol) of goes for the divide and conquer method.

In a Quick sort, we choose a pivot value and use it to guide our iteration through the list. 

As we go through and hit each value, we compare the value to values to the left of it...