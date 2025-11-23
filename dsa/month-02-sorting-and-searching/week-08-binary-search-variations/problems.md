# Week 08: Binary Search Variations - Problems

## Problem Set

### Problem 1: Search in Rotated Sorted Array
**Difficulty:** Medium

There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k.

**Example:**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Constraints:**
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique

---

### Problem 2: Search in Rotated Sorted Array II
**Difficulty:** Medium

There is an integer array nums sorted in non-decreasing order (with possible duplicates). Prior to being passed to your function, nums is rotated at an unknown pivot index k.

**Example:**
```
Input: nums = [1,0,1,1,1], target = 0
Output: true
```

**Constraints:**
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- nums is rotated at some unknown pivot index k

---

### Problem 3: Find Peak Element
**Difficulty:** Medium

A peak element is an element that is strictly greater than its neighbors. Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

**Example:**
```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

**Constraints:**
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1

---

### Problem 4: Find Minimum in Rotated Sorted Array
**Difficulty:** Medium

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Find the minimum element in the array.

**Example:**
```
Input: nums = [3,4,5,1,2]
Output: 1
```

**Constraints:**
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000

---

### Problem 5: Find Minimum in Rotated Sorted Array II
**Difficulty:** Hard

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

**Example:**
```
Input: nums = [1,3,5]
Output: 1

Input: nums = [11,13,15,17]
Output: 11
```

**Constraints:**
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000

---

### Problem 6: Find the Duplicate Number
**Difficulty:** Medium

Given an array of n + 1 integers where each integer is in the range [1, n] inclusive, there is always exactly one duplicate number. Find the duplicate number without modifying the array and using only constant extra space.

**Example:**
```
Input: nums = [1,3,4,2,2]
Output: 2
```

**Constraints:**
- 1 <= n <= 3 * 10^4
- nums.length == n + 1
- 1 <= nums[i] <= n

## Submission Guidelines

1. Choose at least 4 problems to solve
2. Implement in your preferred language
3. Place solutions in `solutions/[language]/` folder
4. Include time and space complexity analysis
5. Explain your approach for handling special cases
6. Test with rotated, duplicated, and edge case inputs
7. Compare with linear search approaches
