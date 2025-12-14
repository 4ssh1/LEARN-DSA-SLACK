class ArrayProblems:
    @staticmethod
    def two_sum(nums, target):
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i

    @staticmethod
    def best_time_to_sell(prices):
        
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:    
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit
    
    @staticmethod
    def contains_duplicate(nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    @staticmethod
    def valid_parentheses(s):
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return not stack # True if stack is empty, else False\
    
    @staticmethod
    def majority_element(nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

    @staticmethod
    def remove_duplicates(nums):
        if not nums:
            return 0

        next_index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[next_index] = nums[i]
                next_index += 1

        return next_index    