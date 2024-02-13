# Python algorythms

## Insertion sort
This algorythm sorts an array by shifting unsorted elements from right to left.
Its running time is quadratic O(n<sup>2</sup>) 

## Selection sort
This algorithm finds the smallest element in the unsorted part and place it in the sorted part.
It has quadratic running time O(n<sup>2</sup>)

## Merge Sort
Divide and Conquer algorithm
-   Breaks down the problem into multiple subproblems recursively until they become simple to solve.
-   Solutions are combined to selve the original problem

Running time is O(n * log(n))

## Quick sort
Breaks down a problem into multiple subproblems recursively until they become simple to solve.
Solutions of subproblems are combined to give the final solution.
-   Worst case running time O(n<sup>2</sup>)
-   Best and average case running time O(n * log(n))

-   ### How it works
    -   Choose a pivot element (usually last or random)
    -   Stores elements smaller than pivot in the left sub-array and greater element in the right sub-array
    -   Call quick sort recursively on left sub-array and same on right sub-array