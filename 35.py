'''
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    result = []
    if target in nums:
        return nums.index(target)
    else:
        for num in nums:
            if num > target:
                add = nums.index(num)
                [result.append(x) for x in nums[:add]]
                result.append(target)
                [result.append(x) for x in nums[add:]]
                return result.index(target)
    nums.append(target)
    return nums.index(target)


if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 5))
    print(searchInsert([1,3,5,6], 2))
    print(searchInsert([1,3,5,6], 7))
