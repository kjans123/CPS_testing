def test_MaxDiffr():
    from maxDifference06 import MaxDifference
    listV = [1, 2, 3, 6, 10]
    firstDiff = MaxDifference(listV)
    assert firstDiff.maxVal == 4
    assert firstDiff.maxVal >= 0
    listV2 = [1.1, 2.2, 3.6, 8.9]
    secondDiff = MaxDifference(listV2)
    assert secondDiff.maxVal == 5.3


def test_correctExcp():
    import pytest
    import math
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
    with pytest.raises(TypeError, message="Expecting TypeError"):
        numTest = 1 + "e"
    with pytest.raises(ValueError, message="Expecting ValueError"):
        numTest = math.sqrt(-1)
