# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/6/17
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        "回溯"
        result, counter = [], len(nums)
        def helper(res, nums):
            if len(res) == counter:
                result.append(res[:])
                return
            for i in range(counter):
                current_value = nums[i]
                res += [current_value]
                nums.pop(i)
                helper(res, nums)
                nums = current_value
        helper([], nums)
        return result

if __name__ == '__main__':
    test = Solution()
    print(test.permute([1,2,3]))



