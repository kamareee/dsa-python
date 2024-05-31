"""
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
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = int(len(nums) / 2)
        position = []

        if len(nums) == 1:
            if target == nums[0]:
                return nums
        if start == 0:
            return [-1, -1]

        # Check if the target is in the left half of the list
        if target < nums[start]:
            for i in range(start - 1, -1, -1):
                if nums[i] == target:
                    # position.append(i)
                    position.insert(0, i)
                else:
                    break

        # Check if the target is in the right half of the list
        elif target > nums[start]:
            for i in range(start + 1, len(nums)):
                if nums[i] == target:
                    position.append(i)
                else:
                    break

        # Check if the target is at the midpoint
        else:
            position.append(start)
            for i in range(start - 1, -1, -1):
                if nums[i] == target:
                    position.insert(0, i)
                else:
                    break
            for i in range(start + 1, len(nums)):
                if nums[i] == target:
                    position.append(i)
                else:
                    break

        # Return the result
        if len(position) == 0:
            return [-1, -1]
        else:
            return [position[0], position[-1]]
