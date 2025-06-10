#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Hello my name is Tae Yoon Lee, my matriculation number is 38321127

# 1. Input the text and make it readable 


import time
import matplotlib.pyplot as plt

file = open("data.txt", "r")
arr = []

for i in file.readlines():
    arr.append(float(i))

file.close()



bubble_sorted_array = arr.copy()
start = time.time()

for i in range(0, len(bubble_sorted_array)-1):
    for j in range(0, len(bubble_sorted_array)-i-1):
        if bubble_sorted_array[j] > bubble_sorted_array[j+1]:
            t = bubble_sorted_array[j]
            bubble_sorted_array[j] = bubble_sorted_array[j+1]
            bubble_sorted_array[j+1] = t

end = time.time()
bubble_sort_elapse = end-start
print("Bubble Sort Execution Time/Elapsed Time:", bubble_sort_elapse)


# My Matriculation number ends with 7, so I'll be using Counting Sort
counting_sorted_array = arr.copy()
start = time.time()

def countSort(arr):
    output = [0 for i in range(counting_sorted_array)]
    count = [0 for i in range(counting_sorted_array)]
    ans = ["" for _ in counting_sorted_array]
    for i in arr:
        count[ord(i)] += 1
    for i in range(counting_sorted_array):
        count[i] += count[i-1]
    for i in range(len(counting_sorted_array)):
        output[count[ord(arr[i])]-1] = counting_sorted_array[i]
        count[ord(counting_sorted_array[i])] -= 1
    for i in range(len(counting_sorted_array)):
        ans[i] = output[i]
    return ans

end = time.time()

counting_sort_elapse = end-start
print("Counting Sort Execution Time/Elapsed Time:", counting_sort_elapse)

print()

#choose what is the algorithm that is faster and the speed up percentage 
if bubble_sort_elapse > counting_sort_elapse:
    print(f"Counting Sort is faster. {(bubble_sort_elapse + counting_sort_elapse)/2}% ")
    plt.plot(bubble_sorted_array)
    plt.show()
else:
    print(f"Bubble Sort is faster. {(bubble_sort_elapse + counting_sort_elapse)/2}% ")
    plt.plot(counting_sorted_array)
    plt.show()


# In[ ]:




