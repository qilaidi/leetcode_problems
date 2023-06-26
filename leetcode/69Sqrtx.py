class Solution:
    def mySqrt(self, x: int) -> int:
        upn, lown, mid = x, 0, 0
        while lown < upn - 1:
            mid = (upn - lown) // 2 + lown
            value = mid * mid
            if value == x:
                return mid
            elif value > x:
                upn = mid
            else:
                lown = mid
        return lown if x > 0 else 0


if __name__ == '__main__':
    test = Solution()
    assert test.mySqrt(4) == 2
    assert test.mySqrt(8) == 2
    assert test.mySqrt(9) == 3
    assert test.mySqrt(0) == 0
