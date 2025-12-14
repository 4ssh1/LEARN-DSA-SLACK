from array_problem import ArrayProblems

def test_two_sum_found():
    assert ArrayProblems.two_sum([1, 3, 5, 6, 7], 7) == [0, 3]

    assert ArrayProblems.two_sum([1, 2, 5, 6, 8, 11], 19) == [4, 5]

def test_max_profit():
    assert ArrayProblems.best_time_to_sell([7, 1, 5, 3, 6, 4]) == 5

    assert ArrayProblems.best_time_to_sell([7, 6, 4, 3, 1]) == 0

def test_contains_duplicate():
    assert ArrayProblems.contains_duplicate([1, 2, 3, 1]) is True

    assert ArrayProblems.contains_duplicate([1, 2, 3, 4]) is False 

def test_valid_parentheses():
    assert ArrayProblems.valid_parentheses("()") is True

    assert ArrayProblems.valid_parentheses("()[]{}") is True

    assert ArrayProblems.valid_parentheses("(]") is False  

def test_majority_element():
    assert ArrayProblems.majority_element([3, 2, 3]) == 3

    assert ArrayProblems.majority_element([2, 2, 1, 1, 1, 2, 2]) == 2     


def test_remove_duplicates():
    assert ArrayProblems.remove_duplicates([1, 1, 2]) == 2

    assert ArrayProblems.remove_duplicates([0,0,1,1,1,2,2,3,3,4]) == 5