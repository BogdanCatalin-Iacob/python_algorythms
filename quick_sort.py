'''
Quick sort algorithm
'''

def quick_sort(arr, left_index, right_index):
    '''
    Sort an array by dividing it in smaller arrays
    -   left_index / right_index determine the part of the array to be sorted
    '''
    if left_index < right_index:
        partition_position = partition(arr, left_index, right_index)
        quick_sort(arr, left_index, partition_position - 1)
        quick_sort(arr, partition_position + 1, right_index)


def partition(arr, left_index, right_index):
    '''
    Returns the index of the pivot element after the first step of quick sort
    '''
    i = left_index
    j = right_index - 1
    pivot = arr[right_index]

    while i < j:
        while i < right_index and arr[i] < pivot:
            i += 1
        while j > left_index and arr[j] >= pivot:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right_index] = arr[right_index], arr[i]
    
    return i


arr = [2, 15, 10, 45, 3, 7, 1, 25]

quick_sort(arr, 0, len(arr) - 1)
print(arr)
