import pytest

def test_int_add():
    assert 1 + 2 == 3
    assert 2 + (-2) == 0
    assert -2 + 1 == -1
    assert -3 + (-3) == -6


@pytest.mark.parametrize('a, b, c', [(1, 2, -1),
                                     (-1, 2, -3),
                                     (1, -2, 3),
                                     (-1, -2, 1)])
def test_int_subtraction(a, b, c):
    assert a - b == c

def test_int_zero_div():
    with pytest.raises(ZeroDivisionError):
        assert 0 ** -1

def test_dict_update():
    d = {1: 2, 5: 6}
    d.update({3: 4, 7: 8})
    assert d == {1: 2, 3: 4, 5: 6, 7: 8}
    d.update({1: -2, 8: 9})
    assert d == {1: -2, 3: 4, 5: 6, 7: 8, 8: 9}


@pytest.mark.parametrize('dct, items', [({1: 2, 2: 3}, [(1, 2), (2, 3)]),
                                        ({'1': 2, 2: '3', 'set': {1, 5, 2}}, [('1', 2), (2, '3'), ('set', {1, 2, 5})])])
def test_dict_items(dct, items):
    assert list(dct.items()) == items

def test_dict_key_error():
    d = {1: -2, 'v': 4, 5: 6, 0.5: {3, 4}, 8: 9}
    with pytest.raises(KeyError):
        assert d[-2]
