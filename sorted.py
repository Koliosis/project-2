import random

#set random seed to test results and create randomized list
random.seed(30)
rand_list = random.sample(range(0, 100000000), 10000000)
simp_list = [5,3,7,8,1,2,9,10,6,4]

#create swap function to make sorting easier
def swap(lyst, i, j):
    lyst[i], lyst[j] = lyst[j], lyst[i]
    return lyst

#create insertion sort function
def insertion_sort(lyst):
    for i in lyst:
        if lyst[i + 1] < lyst[i]:
            temp = lyst[i + 1]
            while temp < lyst[i]:
                i -= 1
            lyst.insert(i - 1, temp)
        i += 1
    return lyst



def merge_sort(lyst):
    pass

#Put in my sorting function so that my searching functions work
def bubble_sort(lyst):
    """"""
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i-1)
            i += 1
        n -= 1
    return lyst

print(insertion_sort(simp_list))