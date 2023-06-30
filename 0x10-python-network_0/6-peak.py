#!/usr/bin/python3
"""
Definition for a function that finds a peak in a list of unsorted integers.
"""


def find_peak(nums):
    """Finds and returns a peak in a list of unsorted integers"""
    if not nums:
        return (None)
    size = len(nums)
    if size > 1 and nums[0] > nums[1]:
        return (nums[0])
    if size > 1 and nums[size - 1] > nums[size - 2]:
        return (nums[size - 1])

    for i in range(1, size - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return (nums[i])
    return (nums[0])
