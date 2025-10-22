import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.app import dedupe, add_numbers

def test_dedupe():
    assert dedupe([1, 2, 2, 3]) == [1, 2, 3]
    assert dedupe(['a', 'b', 'a']) == ['a', 'b']
    assert dedupe([]) == []

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_integration():
    # Test that both functions work together
    result = add_numbers(10, add_numbers(5, 3))
    assert result == 18