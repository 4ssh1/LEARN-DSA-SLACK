# Week 07: Binary Search Fundamentals - Problems

## Problem Set

### Problem 1: Binary Search
**Difficulty:** Easy

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

**Example:**
```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4.
```

**Constraints:**
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique

---

### Problem 2: First Bad Version
**Difficulty:** Easy

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions, and you want to find the first bad one. You are given an API bool isBadVersion(version) which will return whether version is bad.

**Example:**
```
Input: n = 5, bad = 4
Output: 4
Explanation: The first bad version is 4.
```

**Constraints:**
- 1 <= bad <= n <= 2^31 - 1

---

### Problem 3: Search Insert Position
**Difficulty:** Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

**Example:**
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Constraints:**
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- -10^4 <= target <= 10^4

---

### Problem 4: Find First and Last Position of Element in Sorted Array
**Difficulty:** Medium

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

**Example:**
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

**Constraints:**
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

---

### Problem 5: Sqrt(x)
**Difficulty:** Easy

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer and the square root has to be truncated toward zero, the decimal part will be truncated.

**Example:**
```
Input: x = 4
Output: 2

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., truncated to 2.
```

**Constraints:**
- 0 <= x <= 2^31 - 1

---

### Problem 6: Guess Number Higher or Lower
**Difficulty:** Easy

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:
- -1: Your guess is higher than my number
- 1: Your guess is lower than my number
- 0: your guess is equal to my number

**Example:**
```
Input: n = 10, pick = 6
Output: 6
```

## Submission Guidelines

1. Choose at least 4 problems to solve
2. Implement in your preferred language
3. Place solutions in `solutions/[language]/` folder
4. Include time and space complexity analysis
5. Handle all edge cases carefully
6. Test with boundary conditions
7. Verify sorted array requirement
