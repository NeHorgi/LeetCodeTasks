'''
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''


from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    result = []
    if target in nums:
        if nums.count(target) < 2:
            return [nums.index(target), nums.index(target)]
        elif nums.count(target) > 2:
            first = nums.index(target)
            for num in range(len(nums) - 1, -1, -1):
                if nums[num] == target:
                    second = num
                    break
            return [first, second]
        result.append(nums.index(target))
        nums[nums.index(target)] = None
        result.append(nums.index(target))
        return result
    else:
        return [-1, -1]


if __name__ == '__main__':
    print(searchRange([5,7,7,8,8,10], 8))
    print(searchRange([5,7,7,8,8,10], 6))
    print(searchRange([], 0))
