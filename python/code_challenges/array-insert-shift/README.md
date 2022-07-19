# Insert and Shift and Array at Middle Index
Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Array-Insert-Shift-img]()

## Approach & Efficiency
<!-- What approach did you take? Discuss Why. What is the Big O space/time for this approach? -->
- The code I want to depict in this process is as follows:

```python
def ins_and_shift(arr, val):
  print('length of input array: ', len(arr))
  midIndex = len(arr) // 2
  print('midIndex: ', midIndex)
  newList = []
  if len(arr) % 2 == 0:
    print('len is even?: ', len(arr) % 2 == 0)
    for x in arr:
      if arr.index(x) < midIndex:
        print(arr.index(x))
        newList.append(x)
        print(newList)
      elif arr.index(x) == midIndex:
        print(arr.index(x))
        newList.append(val)
        newList.append(x)
        print(newList)
      else:
        print('this', arr.index(x))
        newList.append(x)
        print(newList)
  else:
    print('len is even?: ', len(arr) % 2 == 0)
    for x in arr:
      if arr.index(x) < midIndex:
        print(arr.index(x))
        newList.append(x)
        print(newList)
      elif arr.index(x) == midIndex:
        print(arr.index(x))
        newList.append(x)
        newList.append(val)
        print(newList)
      else:
        print('this', arr.index(x))
        newList.append(x)
        print(newList)

  print('\n length of input array: ', len(arr))
  print('\n input arr: \n', arr, '\n')
  print('length of output array: ', len(newList))
  print('\n output arr: \n', newList)

exArr = [2,4,6,-8]
exArr2 = [42,8,15,23,42]
ins_and_shift(exArr, 5)
ins_and_shift(exArr2, 16)
```