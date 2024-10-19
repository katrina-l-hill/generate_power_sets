# test.py

from app import generate_power_set

# Normal test cases
def test_three_elements():
    input_set = {'a', 'b', 'c'}
    expected_output = [
        frozenset(), frozenset({'a'}), frozenset({'b'}), frozenset({'c'}),
        frozenset({'a', 'b'}), frozenset({'a', 'c'}), frozenset({'b', 'c'}),
        frozenset({'a', 'b', 'c'})
    ]
    result = generate_power_set(input_set)
    assert set(result) == set(expected_output)

def test_two_elements():
    input_set = {'x', 'y'}
    expected_output = [
        frozenset(), frozenset({'x'}), frozenset({'y'}), frozenset({'x', 'y'})
    ]
    result = generate_power_set(input_set)
    assert set(result) == set(expected_output)

def test_four_elements():
    input_set = {1, 2, 3, 4}
    expected_output = [
        frozenset(), frozenset({1}), frozenset({2}), frozenset({3}), frozenset({4}),
        frozenset({1, 2}), frozenset({1, 3}), frozenset({1, 4}), frozenset({2, 3}),
        frozenset({2, 4}), frozenset({3, 4}), frozenset({1, 2, 3}),
        frozenset({1, 2, 4}), frozenset({1, 3, 4}), frozenset({2, 3, 4}),
        frozenset({1, 2, 3, 4})
    ]
    result = generate_power_set(input_set)
    assert set(result) == set(expected_output)

# Edge test cases
def test_empty_set():
    input_set = set()
    expected_output = [frozenset()]
    result = generate_power_set(input_set)
    assert set(result) == set(expected_output)

def test_single_element():
    input_set = {'z'}
    expected_output = [frozenset(), frozenset({'z'})]
    result = generate_power_set(input_set)
    assert set(result) == set(expected_output)

def test_duplicates():
    input_set = {'a', 'a', 'b'}
    expected_output = [
        frozenset(), frozenset({'a'}), frozenset({'b'}), frozenset({'a', 'b'})
    ]
    result = generate_power_set(input_set)
    assert set(result) == set(expected_output)
