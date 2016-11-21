def find_turning_point(array, start, end):
    mid = (start + end) // 2
    
    if array[mid-1] > array[mid] > array[mid+1]:
        if find_turning_point(array, start, mid):
            return find_turning_point(array, start, mid)
    if array[mid-1] < array[mid] > array[mid+1]:
        return 'Turning point is {0} on index {1}.'.format(array[mid+1], mid+1)
    if array[mid-1] < array[mid] < array[mid+1]:
        return find_turning_point(array, mid, end)

lists = [[1, 6, 4, 3, 2],
[1, 3, 7, 9, 4, 2],
[1, 4, 5, 2]]
for l in lists:
#    print('Turning point for ', l, ' is: ', 
#          find_turning_point(l, 0, len(l)-1))
    print(find_turning_point(l, 0, len(l)-1)
