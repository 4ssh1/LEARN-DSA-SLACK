# Week 01: Array Basics - Problems

## Problem Set

### Problem 1: Two Sum
**Difficulty:** Easy

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. You may assume each input has exactly one solution, and you may not use the same element twice.

**Example:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9, so we return [0, 1].
```

**Constraints:**
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

---

### Problem 2: Best Time to Buy and Sell Stock
**Difficulty:** Easy

You are given an array `prices` where `prices[i]` is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy and a different day in the future to sell your stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

**Example:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
```

**Constraints:**
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

### Problem 3: Contains Duplicate
**Difficulty:** Easy

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Example:**
```
Input: nums = [1,2,3,1]
Output: true
```

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

### Problem 4: Valid Parentheses
**Difficulty:** Easy

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example:**
```
Input: s = "()[]{}"
Output: true
```

**Constraints:**
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`

---

### Problem 5: Majority Element
**Difficulty:** Easy

Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example:**
```
Input: nums = [3,2,3]
Output: 3
```

**Constraints:**
- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

**Follow-up:** Could you solve the problem in linear time and in O(1) space?

---

### Problem 6: Remove Duplicates from Sorted Array
**Difficulty:** Easy

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

**Example:**
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned k.
```

**Constraints:**
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order

---

## Submission Guidelines

1. Choose at least 3 problems to solve
2. Implement in your preferred language
3. Place solution in the appropriate `solutions/[language]/` folder
4. Include time and space complexity analysis
5. Test with provided examples and edge cases
6. Consider multiple approaches and optimizations
