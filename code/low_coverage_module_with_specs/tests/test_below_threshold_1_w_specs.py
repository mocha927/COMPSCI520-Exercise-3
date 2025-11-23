from low_coverage_code.below_threshold_1 import below_threshold
import pytest

def test_res_equals_list_comprehension_and_sum_equivalence():
    cases = [
        ([1, 2, 3], 5),
        ([0, 1, 2], 2),
        ([5, 6], 10),
        ([], 1),
    ]
    for l, t in cases:
        res = below_threshold(l, t)
        assert res == (len([x for x in l if x < t]) == len(l))
        assert res == (sum(1 for x in l if x < t) == len(l))

def test_res_equals_no_elements_ge_t():
    l = [1, 2, 3]
    t = 4
    res = below_threshold(l, t)
    assert res == (len([x for x in l if x >= t]) == 0)

def test_non_empty_and_max_relation_for_nonempty():
    l = [1, 2, 3]
    t = 4
    assert len(l) != 0
    res = below_threshold(l, t)
    # spec: (len(l) == 0) or (res == (max(l) < t))
    assert (len(l) == 0) or (res == (max(l) < t))

def test_singleton_behaviour():
    l1 = [4]
    t1 = 5
    res1 = below_threshold(l1, t1)
    assert res1 == (l1[0] < t1)
    l2 = [5]
    t2 = 5
    res2 = below_threshold(l2, t2)
    assert res2 == (l2[0] < t2)

def test_empty_list_spec_and_nontrivial_cases():
    l = []
    t = 10
    res = below_threshold(l, t)
    # spec: (len(l) == 0) or (res == (max(l) < t)) -> short-circuits for empty list
    assert (len(l) == 0) or (res == (max(l) < t))
    # also verify sum-equivalence for empty list
    assert res == (sum(1 for x in l if x < t) == len(l))