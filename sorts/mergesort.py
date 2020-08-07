import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def merge_sort(sort_me):
    if len(sort_me) >1: 
        mid = len(sort_me)//2
        L = sort_me[:mid]
        R = sort_me[mid:]

        merge_sort(L)
        merge_sort(R)

        i=j=k=0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                sort_me[k] = L[i]
                i+=1
            else:
                sort_me[k] = R[j]
                j+=1

            k+=1
        while i <len(L):
            sort_me[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            sort_me[k] = R[j]
            j+=1
        k+=1


def print_sorted(arr):
    for i in range(len(arr)):
        print(arr[i])

def start_merge_sort(arr):
    merge_sort(arr)
    print_sorted(arr)
