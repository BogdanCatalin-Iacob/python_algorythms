'''
Merge sort algorithm
'''

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0  # left_arr index
        j = 0  # right_arr index
        index = 0  # merged array index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[index] = left_arr[i]
                i += 1
            else:
                arr[index] = right_arr[j]
                j += 1

            index += 1
        
        while i < len(left_arr):
            arr[index] = left_arr[i]
            i += 1
            index += 1
        
        while j< len(right_arr):
            arr[index] = right_arr[j]
            j += 1
            index +=1


arr = [2, 5, 3, 7, 9, 4, 4, 2, 6, 0]

merge_sort(arr)
print(arr)