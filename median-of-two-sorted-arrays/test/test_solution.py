# import pytest
from solution import Solution


class TestSolution:
    """Test if the solution is correct"""

    def test_first(*args):
        """Test function"""

        assert Solution().findMedianSortedArrays(nums1=[1, 3], nums2=[2]) == 2

    def test_second(*args):
        """Test function"""

        assert (
            Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]) == (2 + 3) / 2
        )
