from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temph = {}
        target = len(nums) // 2
        for i in nums:
            if i in temph.keys():
                temph[i] += 1
            else:
                temph[i] = 1
            if temph[i] > target:
                return i


if __name__ == '__main__':
    test = Solution()
    print(test.majorityElement([3, 2, 3]))
    assert test.majorityElement([3, 2, 3]) == 3
    assert test.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert test.majorityElement([2, 1, 1, 1, 1, 2, 2]) == 1
