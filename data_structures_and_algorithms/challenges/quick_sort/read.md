# Challenge Summary
Make a blog post explaining the quick sort algorithm.

## Challenge Description
Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

Once you are done with your article, code a working, tested implementation of Quick Sort based on the pseudocode provided.

## Approach & Efficiency
The approach I took to this was to split the algorithm into three different functions. One to handle the partition, one to swap the pointers values, and another to hold the logic of when to swap and make partitions, called quick_sort.
The efficiency of this algortihm is a time complexity of
O(nlog(n)) at best and O(n^2) at worst. The space complexity is O(nlog(n)) aswell.

## Solution

#### Steps:
1. We need a list to sort, and we need some logic
2. We start by making three functions, one to separate the list, another to pick a pivot point, and lastly one to compare the pointers to the pivot.
3. Whats a pivot you ask? Well its a point we randomly choose in the list that acts as a comparison. Well whats the point of that? Ill tell you, we set up two pointers, a left and a right, and compare their values to the pivot.
4. Now heres a breakdown, First we cut the list in half, and pick the left chunk. We then choose a pivot, ideally somewhere in the middle of the list. Then we set our left pointer to index 0 of the list, and our right pointer to the last index of the list.
5. We then start comparing the left pointer to the pivot, if the value at its current index is less the pivot, we increment the left pointers index up one. If the left pointers value at the current index is greater than or equal to the pivot, we pause the left and start incrementing the right pointer backwards through the list. We do this until we find a value that is less than the pointer.
6. Once we have our pointers aiming at two out of place values, we swap their values at their indices. So the left pointers value becomes the rights value and vice versa.
7. Once that is done, we repeat the process until the left and right pointer are aiming at the same index.
8. We then split the list we were working on in half and repeat.
9. Eventually we will end up with a beautifully sorted list thanks to the quick sort algorithm.



## PseudoCode

ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
