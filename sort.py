"""
Name: Kole Davis
Project: Project 2: Sorting
"""

#import all the things I'm going to need
import random
from time import perf_counter
# from recursioncounter import RecursionCounter
# from arrays import Array
import numpy


#establish random seed
random.seed(30)
#create a test list of random integers from 0 to 1000
test_list = random.sample(range(100000),k=10000)

#create my swap function to make sorting easier
def swap(lyst, i, j):
    lyst[i], lyst[j] = lyst[j], lyst[i]


#Create my quick_sort function
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# Function to do Quick sort
def quick_sort(arr, low, high):
    arr = test_list
    n = len(arr)
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Driver code to test above
# arr = test_list
# n = len(arr)
# quick_sort(arr, 0, n - 1)
# print("Sorted array is:")
# for i in range(n):
#     print("%d" % arr[i]),


#Create my merge_sort function
def merge_sort(lyst):
    #create copybuffer that's the same length as the lyst
    copy_buffer = numpy.zeros_like(lyst)
    #call merge_sort_helper function
    merge_sort_helper(lyst, copy_buffer, 0, len(lyst) - 1)
    return lyst


def merge_sort_helper(lyst, copy_buffer, low, high):
    if low < high:
        #split my list in half
        middle = (low + high) // 2
        #make this recursive
        #first recursive call works with the first half
        merge_sort_helper(lyst, copy_buffer, low, middle)
        #second recursive call helps with the second half
        merge_sort_helper(lyst, copy_buffer, middle + 1, high)
        #call merge function to put everything together in order
        merge(lyst, copy_buffer, low, middle, high)


def merge(lyst, copy_buffer, low, middle, high):
    #create variables for the first items in each list
    i1 = low
    i2 = middle + 1
    #put the lists back together
    for i in range(low,high + 1):
        #basically this section just takes the lists and finds the smallest value and puts it into copy_buffer and repeats that.
        #that way copy_buffer will be 2 lists that are sorted
        if i1 > middle:
            copy_buffer[i] = lyst[i2]
            i2 += 1
        elif i2 > high:
            copy_buffer[i] = lyst [i1]
            i1 += 1
        #its most likely that our sublists will be backwards so if necessary we will need to swap them.
        elif lyst[i1] < lyst[i2]:
            # copy_buffer.reshape(copy_buffer, 1, 1000)
            copy_buffer[i] = lyst[i1]
            i1 += 1
        else:
            copy_buffer[i] = lyst[i2]
            i2 += 1
    #now we need to copy everything from our copy_buffer array back into the list, in order.
    for i in range(low, high + 1):
        lyst[i] = copy_buffer[i]



#Create my insertion_sort function
def insertion_sort(lyst):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        i += 1
    return lyst


#Create my selection_sort function
def selection_sort(lyst):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst) - 1:
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i)
        i += 1
    return lyst


#Copy in the tim_sort function
# Python3 program to perform TimSort.
RUN = 32


# This function sorts array from left index to
# to right index which is of size atmost RUN
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):

        temp = arr[i]
        j = i - 1
        while j >= left and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

    # merge function merges the sorted runs


def mergeTim(arr, l, m, r):
    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l
    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


# iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def timSort(arr):
    # Sort individual subarrays of size RUN
    n = len(arr)
    for i in range(0, n, RUN):
        insertionSort(arr, i, min((i + 31), (n - 1)))

    # start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = RUN
    while size < n:

        # pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):
            # find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))

            # merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            mergeTim(arr, left, mid, right)

        size = 2 * size
    return arr

    # utility function to print the Array


#Create my main function
func_list = [merge_sort,insertion_sort,selection_sort,timSort]
def main(lyst):
    for fn in func_list:
        print(f"Sorting list by {fn.__name__}")
        t1_start = perf_counter()
        print(f"{fn.__name__} sorted {fn(test_list)}")
        t1_stop = perf_counter()
        print(f"sorted in {t1_stop - t1_start} seconds")


if __name__ == "__main__":
    main(test_list)