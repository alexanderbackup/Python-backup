l = [0, 1]

def binary_search(array, start, end, element):
    mid = (start + end) // 2
    if array[mid] == element:
        return mid
    if array[mid] > element:
        return binary_search(array, start, mid-1, element)
    else:
        return binary_search(array, mid+1, end, element)

print(binary_search(l, 0, len(l)-1, 3))
