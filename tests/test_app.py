from src.app import sum, main

def test_sum():
    assert sum(1,3) == 4

def test_sum_with_large_values():
    assert sum(5128793,2690872) == 7819665

def test_sum_with_negatives():
    assert sum(-10,30) == 20

def test_sum_with_wrong_datatypes():
    try:
        sum("a",5)
        assert False
    except TypeError:
        assert True