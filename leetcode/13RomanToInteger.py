class Solution:
    NUM_MAP = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    couple_map = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}

    def romanToInt(self, s: str) -> int:
        res = 0
        tem = ""
        for c in s:
            if not tem:
                if c in self.couple_map.keys():
                    tem = c
                else:
                    res += self.NUM_MAP[c]
            elif tem in self.couple_map.keys() and c in self.couple_map[tem]:
                res += self.NUM_MAP[c] - self.NUM_MAP[tem]
                tem = ""
            elif c in self.couple_map.keys():
                res += self.NUM_MAP[tem]
                tem = c
            else:
                res += self.NUM_MAP[tem] + self.NUM_MAP[c]
                tem = ""
        if tem:
            res += self.NUM_MAP[tem]
        return res


if __name__ == '__main__':
    test = Solution()
    assert(test.romanToInt("III") == 3)
    assert(test.romanToInt("LVIII") == 58)
    assert(test.romanToInt("MCMXCIV") == 1994)
    assert(test.romanToInt("MDCCCLXXXIV") == 1884)
    assert(test.romanToInt("MMMCCLIX") == 3259)
