'''
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
'''
list1=[]
nums.sort()
if nums[-1]!=nums[-2]:
    list1.append(nums[-1])
if nums[0]!=nums[1]:
    list1.append(nums[0])
for i in range(1,len(nums)-1):
    if nums[i]!=nums[i+1] and nums[i]!=nums[i-1]:
        list1.append(nums[i])
return list1