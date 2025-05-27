# Two Sum

## Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Solution (Python)
```python
def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
