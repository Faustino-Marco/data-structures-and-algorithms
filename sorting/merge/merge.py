def merge_sort(data):
    length_of_data = len(data)

    if length_of_data > 1:
        mid = length_of_data // 2
        left = data[0:mid]
        right = data[mid:length_of_data]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, data)

    return data

def merge(left, right, data):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1

        k += 1

    if i == len(left):
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
    else:
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

    return data
