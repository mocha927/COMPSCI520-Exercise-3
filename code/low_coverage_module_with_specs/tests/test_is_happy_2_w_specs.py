import pytest
from low_coverage_code.is_happy_2 import is_happy

def _expected(s):
    return (len(s) >= 3) and all((s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]) for i in range(len(s)-2))

def test_return_type_is_bool():
    cases = [[], [1], [1,2], [1,2,3], [1,1,2,3], [0,1,0,2]]
    for s in cases:
        res = is_happy(s)
        assert isinstance(res, bool)

def test_equivalence_with_spec_on_various_sequences():
    cases = [
        [],
        [1],
        [1,2],
        [1,2,3],
        [1,1,1],
        [1,2,1,2,3],
        [0,0,1,2,3],
        [7,8,9,7]
    ]
    for s in cases:
        res = is_happy(s)
        expected = _expected(s)
        assert res == expected

def test_len_ge_3_example_and_assertion():
    s = [10, 20, 30]
    assert len(s) >= 3
    res = is_happy(s)
    assert res == (len(s) >= 3 and all((s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]) for i in range(len(s)-2)))

def test_len_lt_3_behavior():
    s = [1, 2]
    assert len(s) < 3
    res = is_happy(s)
    # For len(s) < 3 the spec's conditional should hold (left side true), and expected is False
    assert res == _expected(s)

def test_not_res_when_triple_has_equal_elements():
    s = [5, 5, 6, 7]
    # there exists a triple with equal adjacent elements (s[0] == s[1])
    assert any(s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2] for i in range(len(s)-2))
    res = is_happy(s)
    # spec: any(...) == (res == False) when len(s) >= 3
    assert (len(s) < 3) or (any(s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2] for i in range(len(s)-2)) == (res == False))