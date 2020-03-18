# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/22

class Solution:
    def numDecodings(self, s: str) -> int:
        ## 0前面没有数字或数字大于2的时候是不能解码的
        if s[0] == "0":
            return 0
        elif len(s) == 1:
            return 1
        current = x = y = 1
        for i in range(1, len(s)):
            if (s[i] == "0"):
                if s[i - 1] in ("1", "2"):
                    current = x
                else:
                    return 0
            elif s[i-1] == "1" or (s[i-1] == "2" and "1" <= s[i] <= "6"):
                current = x + y
            x, y = y, current
        return current



if __name__ == '__main__':
    test = Solution()
    print(test.numDecodings("12")) # 2
    print(test.numDecodings("226")) #3
    print(test.numDecodings("27")) # 1
    print(test.numDecodings("101")) # 1
    print(test.numDecodings("110")) #1
    print(test.numDecodings("17")) #1