class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            if columnNumber < 26:
                res = chr(columnNumber % 26 + 64) + res
                break
            left = columnNumber % 26
            if left == 0:
                columnNumber = columnNumber // 26 - 1
                res = "Z" + res
            else:
                columnNumber = columnNumber // 26
                res = chr(left + 64) + res
        return res



if __name__ == '__main__':
    test = Solution()

    print(test.convertToTitle(701))
    assert test.convertToTitle(1) == "A"
    assert test.convertToTitle(26) == "Z"
    assert test.convertToTitle(28) == "AB"
    assert test.convertToTitle(52) == "AZ"
    assert test.convertToTitle(78) == "BZ"
    assert test.convertToTitle(701) == "ZY"
    assert test.convertToTitle(2147483647) == "FXSHRXW"
