'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
'''
def validMountainArray(arr):
        inc=0
        dec=0
        if len(arr)==1:
            return False
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                return False
            if arr[i]<arr[i+1]:
                inc=1
            if inc==1 and dec==1:
                if arr[i]<arr[i+1]:
                    return False 
            if arr[i]>arr[i+1]:
                dec=1
                if inc==0:
                    return False
        if inc==0 or dec==0:
            return False
        return True
print(validMountainArray(arr = [3,5,5]))