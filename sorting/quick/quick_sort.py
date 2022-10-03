def quick_sort(nums, left, right):
    if left < right:
        position = piece(nums, left, right)
        quick_sort(nums, left, position - 1)
        quick_sort(nums, position + 1, right)

    return nums

def piece(nums, left, right):
    turn = nums[right]
    low = left - 1

    for i in range(left, right):
        if nums[i] <= turn:
            low += 1
            swap(nums, i, low)

    switch(nums, right, low + 1)

    return low + 1

def switch(nums, i, low):
        nums[i], nums[low] = nums[low], nums[i]