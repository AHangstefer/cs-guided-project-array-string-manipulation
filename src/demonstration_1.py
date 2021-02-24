"""
Given an array of integers `nums`, define a function that returns the
"pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of
that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function 
should return `-1`. If there are more than one "pivot" indexes, then you
should return the left-most "pivot" index.

##UPER
input
-we have an array of integers
-assume array can be empty bc of line 7
-assume it can be positive and negative ints
output
-ints, numbers
-returning a pivot index
-reasonable output number = 0-len-1
-pivot index is not part of the sum (half of each group of numbers equals the same value)


the pivot index of this [11,3,11] is index 1.
the pivot index of this [11,0,0,11] is index (reverence instructions and
                                                return left most one)

PLAN
-"I want to find something in my array"
-search problem
-CHECK EVERY ITEM
-figure out if an item is a pivot index or not,
-figure out what to do when we find it
*describe problem in plain english to get a good idea going
for each index: starting at index = 0 (bc we're staring on the left(directions))
sum all numbers to the 
  sumL =  if no items, sum = 0
and then to the right
   sumR = if no items, sum = 0
compare: sumL and sumR == #we only care if they're equal
    if false:
        move on
    if true:
        return index?
return -1

[:] where to start: where to end (last value is not included)




                                             

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
def pivot_index(nums):
    for i in range(len(nums)):
        #check if pivot
        #sum all left of index
        left_sub_list = nums[0:i]
        sum_l = sum(left_sub_list)
        #then sum all right
        right_sub_list = nums[i+1:]
        sum_r = sum(right_sub_list)
        if sum_l == sum_r:
            return i


    
    return -1
   
print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1,2,3]))
print(pivot_index([1]))

