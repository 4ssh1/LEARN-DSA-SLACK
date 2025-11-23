# Problem Solving Template

A systematic approach to solving DSA problems effectively.

## Step 1: Understand the Problem

- [ ] Read the problem statement carefully
- [ ] Identify inputs and outputs
- [ ] Note any constraints
- [ ] Look for edge cases
- [ ] Ask clarifying questions if needed

**Example questions:**
- What's the range of inputs?
- Can there be negative numbers?
- Are duplicates allowed?
- What about empty inputs?

## Step 2: Work Through Examples

- [ ] Use the provided examples
- [ ] Create your own test cases
- [ ] Think about edge cases
- [ ] Trace through your logic manually

**Edge cases to consider:**
- Empty input
- Single element
- Duplicates
- Maximum/minimum values
- Negative numbers

## Step 3: Brainstorm Solutions

- [ ] Generate multiple approaches
- [ ] Don't dismiss ideas too quickly
- [ ] Consider brute force first
- [ ] Think about optimization opportunities

**Common patterns to consider:**
- Brute force
- Two pointers
- Sliding window
- Hash map/set
- Sorting
- Binary search
- Dynamic programming
- Recursion/Backtracking

## Step 4: Analyze Complexity

For each approach:
- [ ] Calculate time complexity
- [ ] Calculate space complexity
- [ ] Compare with alternatives
- [ ] Choose the best solution

**Formula:**
- Loops: O(n), nested loops: O(n²)
- Hash operations: O(1) average
- Sorting: O(n log n)
- Recursion depth: O(n) space

## Step 5: Code the Solution

- [ ] Write clean, readable code
- [ ] Use meaningful variable names
- [ ] Add comments for complex logic
- [ ] Handle edge cases explicitly

**Best practices:**
- One responsibility per function
- Consistent indentation
- Avoid magic numbers
- Test as you code

## Step 6: Test Thoroughly

- [ ] Test with provided examples
- [ ] Test edge cases
- [ ] Test with different input sizes
- [ ] Check for off-by-one errors

**Testing checklist:**
- Normal cases
- Edge cases
- Boundary conditions
- Invalid inputs

## Step 7: Optimize if Needed

- [ ] Review your solution
- [ ] Can you improve time complexity?
- [ ] Can you improve space complexity?
- [ ] Is readability maintained?

## Step 8: Review & Learn

- [ ] Check other solutions
- [ ] Learn alternative approaches
- [ ] Identify patterns for future problems
- [ ] Document key insights

---

## Template Code Structure

```python
def solve(input_data):
    """
    Solve the problem.
    
    Args:
        input_data: Description of input
        
    Returns:
        The solution
        
    Time: O(?)
    Space: O(?)
    """
    # Input validation
    if not input_data:
        return None
    
    # Main solution logic
    result = None
    
    # Return result
    return result
```
