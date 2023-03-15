'''
169. Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

from typing import List


def majorityElement(nums: List[int]) -> int:
    set_list = set(nums)
    majority_element = 0
    majority_count = 0
    for element in set_list:
        if nums.count(element) > majority_count:
            majority_count = nums.count(element)
            majority_element = element
    return majority_element


if __name__ == '__main__':
    print(majorityElement([3,2,3]))
    print(majorityElement([2,2,1,1,1,2,2]))
