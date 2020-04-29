# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/4/28
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        """执行用时 :68 ms, 在所有 Python3 提交中击败了93.71%的用户"""
        # 用deque代替queue性能有所提升
        if len(nums) < k or k == 0:
            return []
        else:
            result, curr_max_list, queue = [], [], deque(nums[:k])
            curr_max = max(queue)
            result.append(curr_max)
            curr_max_list.append(curr_max)
            for val in nums[k:]:
                tem = queue.popleft()
                if tem == curr_max_list[-1]:
                    curr_max_list.pop()
                queue.append(val)
                if curr_max_list and curr_max_list[-1] == val:
                    curr_max_list.append(val)
                elif curr_max_list and curr_max_list[-1] < val:
                    curr_max_list = [val]
                elif not curr_max_list:
                    curr_max_list.append(max(queue))
                result.append(curr_max_list[-1])
        return result

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """暴力"""
        n = len(nums)
        if n < k or k == 0:
            return []
        else:
            left, right, result = 0, k, []
            while right <= n:
                result.append(max(nums[left:right]))
                left += 1
                right += 1
        return result

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n < k or k <= 0:
            return []
        left = n * [0]
        right = n * [0]
        left[0], right[n-1] = nums[0], nums[n-1]

        # generate left and right
        for i in range(1, n):
            # block start
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])

            j = n - 1 - i
            # block end
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i+k-1], right[i]))

        return output


if __name__ == '__main__':
    test = Solution()
    print(test.maxSlidingWindow([], 0))
    print(test.maxSlidingWindow([], 3))
    print(test.maxSlidingWindow([1, 2, 3], 3))
    print(test.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    print(test.maxSlidingWindow([1,3,1,2,0,5], 3))
    print(test.maxSlidingWindow([-95,92,-85,59,-59,-14,88,-39,2,92,94,79,78,-58,37,48,63,-91,91,74,-28,39,90,-9,-72,-88,-72,93,38,14,-83,-2,21,4,-75,-65,3,63,100,59,-48,43,35,-49,48,-36,-64,-13,-7,-29,87,34,56,-39,-5,-27,-28,10,-57,100,-43,-98,19,-59,78,-28,-91,67,41,-64,76,5,-58,-89,83,26,-7,-82,-32,-76,86,52,-6,84,20,51,-86,26,46,35,-23,30,-51,54,19,30,27,80,45,22], 10))

