from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            j = 1
            cur = [1]
            while j < i:
                if i == 1:
                    cur.append(res[i-1][j-1] * 2)
                else:
                    cur.append(res[i-1][j-1] + res[i-1][j])
                j += 1
            cur.append(1)
            res.append(cur)
        return res

    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            cur_len = i + 1
            cur = [1] * cur_len
            if cur_len > 1:
                for j in range(1, cur_len-1):
                    cur[j] = cur[-j-1] = res[i-1][j-1] + res[i-1][j]
                # if cur_len % 2 != 0:
                #     index = (cur_len//2)+1
                #     cur[index] = res[i-1][index-1] + res[i-1][index]
            res.append(cur)
        return res


if __name__ == '__main__':
    test = Solution()
    result = test.generate(5)
    print(result)
    assert result == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]