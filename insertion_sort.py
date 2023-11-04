'''
Insertion sort algorythm
'''

def insertion_sort(arr):
    '''
    Sort a given array
    '''

    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j-1] and j > 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

numbers = [9, 3, 6, 1, 8, 4, 5, 2]

words = ['car', 'plane', 'bus', 'tractor', 'cart']

insertion_sort(numbers)
insertion_sort(words)

print(numbers)
print(words)
