import pytest
from sorting.merge.merge import merge, merge_sort
# @pytest.mark.skip("pending")
def test_merge_sort():
    actual = merge_sort([4, 6, 5, 1, 34, 23])
    expected = [1, 4, 5, 6, 23, 34]
    assert actual == expected

# @pytest.mark.skip("pending")
def test_merge_sort_backwards():
    actual = merge_sort([3, 2, 1])
    expected = [1, 2, 3]
    assert actual == expected

# @pytest.mark.skip("pending")
def test_merge_sort_duplicates():
    actual = merge_sort([5, 5, 4, 8, 8, 1])
    expected = [1, 4, 5, 5, 8, 8]
    assert actual == expected
