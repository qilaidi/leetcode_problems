# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/4/24
from typing import List


class Solution:
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """三指针从后向前"""
        i, j, k = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]
        print(nums1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)
        print(nums1)

if __name__ == '__main__':
    test = Solution()
    test.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    test.merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)
    test.merge([0,0,3,0,0,0,0,0,0], 3, [-1,1,1,1,2,3], 6)


