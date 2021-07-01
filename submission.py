#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sys

#Merge sort for sorting array elements in nlog(n) time complexity
def merge_sort(arr):
    if len(arr) > 1:
        m_ind = len(arr)//2   #find the middle indices
        l_arr = arr[:m_ind]       #dividing original array in first half
        r_arr = arr[m_ind:]       #dividing original array in second half
 
        merge_sort(l_arr)        #Sorting first half of array
        merge_sort(r_arr)        #Sorting second half of array
 
        x = 0
        y = 0               #initializing looping variable
        z = 0
 
        while x < len(l_arr) and y < len(r_arr):   #sort by comparison
            if l_arr[x] < r_arr[y]:
                arr[z] = l_arr[x]
                x += 1
            else:
                arr[z] = r_arr[y]
                y += 1
            z += 1
 
        while x < len(l_arr):       #checking if any member of array is left
            arr[z] = l_arr[x]
            x += 1
            z += 1
 
        while y < len(r_arr):
            arr[z] = r_arr[y]
            y += 1
            z += 1
  
 #binary search, find element in log(n) time complexity
def binary_search(arr, l, r, x):
    if r >= l:
        mid_ind = l + (r - l) // 2
        
        if arr[mid_ind] == x:   #check if element is at the middle
            return mid_ind
        elif arr[mid_ind] > x:   #if element is smaller than mid then it will be in left sub array otherwise it
            return binary_search(arr, l, mid_ind-1, x)   #will be in right sub array
        else:
            return binary_search(arr, mid_ind + 1, r, x)
    else: 
        return -1           #incase if element not found in array

#function which finds the key which is equal to difference of other two keys
def find_difference(arr,f_elem,l_elem):
    num_found=-1
    for x in range(l_elem):      #outerloop which defines the current closing point of subarray
        cur_val=arr[x]
        for y in range(x):      #innerloop which defines the current starting point of subarray
            cur_val2=arr[y]
            num_found=binary_search(arr,f_elem,x,cur_val-cur_val2) #make pair of every element in subarray and
            if num_found>0:                       #and check if difference exist in array or not
                if cur_val2!=cur_val-cur_val2:    #if difference exist then check if it is not the value itself
                    print(cur_val,cur_val2,cur_val-cur_val2)  #if difference of pair exist as key, print them
                    with open(sys.argv[2], 'a') as f:
                        f.write(str(cur_val)+' '+str(cur_val2)+' '+str(cur_val-cur_val2)+'\n')

#Main function, sorting, finding difference and checking if it exist or not

if __name__ == '__main__':
    arr=[]
    file1=open(sys.argv[1],'r')
    lines = file1.readlines()
    for l in lines:
        arr.append(int(l.replace('\n','')))
    print("Given array is", end="\n")
    print(arr)
    merge_sort(arr)
    print("Sorted array is: ", end="\n")
    print(arr)
    find_difference(arr,0,len(arr))


# In[ ]:




