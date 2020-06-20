# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/6/17
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        "回溯"
        m = len(nums)
        result = []
        def helper(res, nums):
            if len(res) == m:
                result.append(res)
                return
            for i in range(len(nums)):
                temp = nums
                helper(res + [nums[i]], nums[i + 1:])
                nums = temp
        helper([], nums)
        return result





if __name__ == '__main__':
    test = Solution()
    print(test.permute([1,2,3]))



