# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/1/28

class Solution:
    def jump(self, nums):
        steps = 0
        end = 0
        cur_position = 0
        for i in range(len(nums)-1):
            cur_position = max(cur_position, nums[i] + i)
            if i == end:
                end = cur_position
                steps += 1
        return steps




if __name__ == '__main__':
    test = Solution()
    print(test.jump([2,3,1,1,4]))
    print(test.jump([2,1]))
    print(test.jump([2,9,6,5,7,0,7,2,7,9,3,2,2,5,7,8,1,6,6,6,3,5,2,2,6,3]))