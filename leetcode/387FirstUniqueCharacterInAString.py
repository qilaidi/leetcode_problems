# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/16

class Solution:
    def firstUniqChar(self, s):
        s_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict.keys():
                s_dict[s[i]] = [1, i]
            else:
                s_dict[s[i]][0] += 1
        for k, v in s_dict.items():
            if v[0] == 1:
                return v[1]
        else:
            return -1

if __name__ == '__main__':
    test = Solution()
    print(test.firstUniqChar("leetcode")) #0
    print(test.firstUniqChar("loveleetcode")) #2