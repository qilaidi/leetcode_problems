# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/3/12
from typing import List


class Solution:
    def threeSum_brute(self, nums: List[int]) -> List[List[int]]:
        """超时"""
        ress = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b + c == 0:
                        res = sorted([a, b, c])
                        if res not in ress:
                            ress.append(res)
        return ress

    def threeSum_dict(self, nums: List[int]) -> List[List[int]]:
        res = {}
        ress = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]
            d = {}
            for j in range(i+1, len(nums)):
                if nums[j] in d:
                    temp = [nums[j], nums[d[nums[j]]], target]
                    key = "".join(str(x) for x in temp)
                    if key not in res:
                        ress.append(temp)
                        res[key] = True
                else:
                    d[-(target + nums[j])] = j
        return ress

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ress, nums = [], sorted(nums)
        if len(nums) < 3:
            return []
        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                a, b, c = nums[i], nums[j], nums[k]
                if a + b + c == 0:
                    ress.append([a, b, c])
                    while (j < k and nums[j+1] == nums[j]):
                        j += 1
                    while (j < k and nums[k-1] == nums[k]):
                        k -= 1
                    j += 1
                    k -= 1
                elif a + b + c < 0:
                    j += 1
                elif a + b + c > 0:
                    k -= 1
        return ress

if __name__ == '__main__':
    test = Solution()
    print(test.threeSum([-1, 0, 1, 2, -1, -4])) # [[-1,-1,2],[-1,0,1]]
    print(test.threeSum([1,-1,-1,0]))
    print(test.threeSum([0, 0, 0, 0]))
    print(test.threeSum([3,0,-2,-1,1,2])) # [[-2,-1,3],[-2,0,2],[-1,0,1]]