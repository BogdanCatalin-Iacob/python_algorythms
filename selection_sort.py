'''
Selection sort algorithm
'''

def selection_sort(arr):
    '''
    Sort given array from smallest to largest
    '''

    for i in range(0, len(arr) - 1):  # skip the last element
        curr_min_idx = i

        # compare value at curr_min with next elemets
        # and set a new min
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[curr_min_idx]:
                curr_min_idx = j
        
        arr[i], arr[curr_min_idx] = arr[curr_min_idx], arr[i]  # swap elements


arr = [1, 15, 10, 25, 9, 5, 42]

selection_sort(arr)
print(arr)
