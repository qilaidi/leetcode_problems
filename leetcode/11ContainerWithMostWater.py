from typing import List


class Solution1:
    def maxArea(self, height):
        result = []
        self._generate_area(result, 0, len(height) - 1, height)
        return max(result)

    def _generate_area(self, result, left, right, height):
        if left == right:
            return
        result.append(result, (right - left) * min(height[right], height[left]))
        if height[left] > height[right]:
            self._generate_area(result, left, right - 1, height)
        else:
            self._generate_area(result, left + 1, right, height)

    def maxArea_loop(self, height):
        result, left, right = 0, 0, len(height) - 1
        while left < right:
            if height[right] > height[left]:
                result = max(result, (right - left) * height[left])
                left += 1
            else:
                result = max(result, (right - left) * height[right])
                right -= 1
        return result



class Solution:
    def maxArea1(self, height: List[int]) -> int:
        left, right =0, len(height) - 1
        def _generate_area(left, right, res):
            if left == right:
                return res
            a = right - left
            if height[right] <= height[left]:
                res = max(res, a * height[right])
                return _generate_area(left, right-1, res)
            elif height[right] > height[left]:
                res = max(res, a * height[left])
                return _generate_area(left + 1, right, res)
        return _generate_area(0, len(height) - 1, 0)

    def maxArea(self, height: List[int]) -> int:
        res, left, right = 0, 0, len(height) - 1
        while left < right:
            res = max(res, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res

if __name__ == '__main__':
    test = Solution()
    print(test.maxArea([1,8,6,2,5,4,8,3,7]))







