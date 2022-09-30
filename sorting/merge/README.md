# Blog Notes: Merge Sort

## So you wanna Merge-Sort??
Merge sorting is another way of sorting an array, by taking chunks (halves) of the array and sorting them separately and then bringing (merging-dun-dun-dunnn) them all back together to create a fully sorted array!

## Pseudo-Code
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Python-Code

### Input
Here's our input list:
`[8,4,23,42,16,15]`


## Stepthrough
So basically, the list is chopped in half as many times as possible, then sorted and rejoined again as follows:

[8, 4, 23] & [42, 16, 15]

then again...

[8, 4] & [23], [42, 16] & [15]

Then these figures are sorted and merged back into one another sequentially like this:

[4, 8, 23] & [15, 16, 42]

Then, finally:

[4, 8, 15, 16, 23, 42]

Voila!!
