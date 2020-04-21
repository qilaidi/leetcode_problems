# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/4/7
from typing import List


class Solution:
    def rotate_1(self, nums: List[int], k: int) -> None:
        """执行用时 :36 ms, 在所有 Python3 提交中击败了93.30%的用户"""
        length = len(nums)
        if length <= k:
            real_len = k%length
            for i in range(real_len):
                nums[:] = [nums.pop()] + nums
        else:
            nums[:] = nums[-k:] + nums[:-k]
        print(nums)

    def rotate(self, nums: List[int], k: int) -> None:
        real_len, length, start, count = k%len(nums), len(nums), 0, 0
        if length <= 1 or k < 1 or k == length:
            return
        while count < length:
            i = start
            temp = nums[i]
            while True:
                count += 1
                i = (i + real_len) % length
                nums[i], temp = temp, nums[i]
                if start == i:
                    break
            start += 1
        print(nums)





if __name__ == '__main__':
    test = Solution()
    test.rotate([1,2,3,4,5,6,7], 3) #[5, 6, 7, 1, 2, 3, 4]
    test.rotate([1,2,3,4,5,6], 2) #[5,6,1,2,3,4]
    test.rotate([1,2,3,4,5,6], 3) #[4,5,6,1,2,3]
    test.rotate([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54], 45) #[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,1,2,3,4,5,6,7,8,9]
    test.rotate([1,2], 3) #[2, 1]
    test.rotate([1,2], 2) #[1, 2]
    test.rotate([1,2,3], 5) #[2, 3, 1]