# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/6/23

class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary2(self, a: str, b: str) -> str:
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), "1") + "0"
        elif a[-1] == "0" and b[-1] == "0":
            return self.addBinary(a[:-1], b[:-1]) + "0"
        else:
            return self.addBinary(a[:-1], b[:-1]) + "1"

    def addBinary(self, a: str, b: str) -> str:
        return "{:b}".format(int(a, 2) + int(b, 2))





if __name__ == '__main__':
    test = Solution()
    print(test.addBinary("11", "1"))