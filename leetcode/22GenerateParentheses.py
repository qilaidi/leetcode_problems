class Solution:
    def generateParenthesis_1(self, n):
        result = []
        self.generateParenthesis_1(n, n, "", result)
        return result

    def generate_parenthesis_1(self, left, right, s, result):
        if right == 0:
            result.append(s)
            return result
        if left > 0:
            self.generateParenthesis_1(left - 1, right, s + "(", result)
        if right > left:
            self.generateParenthesis_1(left, right - 1, s + ")", result)

    def generateParenthesis_bfs(self, n):
        process = [["(", n-1, n]]
        results = []
        while process:
            current, left, right = process.pop(0)
            if len(current) == n * 2:
                results.append(current)
            if left > 0:
                process.append([current + "(", left - 1, right])
            if right > left:
                process.append([current + ")", left, right - 1])
        return results

    def generateParenthesis_2(self, n):
        result = []
        self.generate_parenthesis_2(n, n, "", result)
        return result

    def generate_parenthesis_2(self, left, right, res, result):
        if left == right == 0:
            result.append(res)
            return result
        if left > 0:
            self.generate_parenthesis_2(left - 1, right, res + "(", result)
        if right > left:
            self.generate_parenthesis_2(left, right - 1, res + ")", result)

    def generateParenthesis_dp1(self, n):
        """DP"""
        total = [[""], ["()"]]
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        for i in range(2, n+1):
            temp_list = []
            for j in range(i):
                p_list = total[j]
                q_list = total[i-1-j]
                for k1 in p_list:
                    for k2 in q_list:
                        temp_list.append("(" + k1 + ")" + k2)
            total.append(temp_list)
        return total[n]

    def generateParenthesis1(self, n):
        """3 dfs"""
        result = []
        def generate_parenthesis(left, right, res, result):
            if right == 0:
                result.append(res)
                return result
            if left > 0:
                generate_parenthesis(left-1, right, res+"(", result)
            if right > left:
                generate_parenthesis(left, right-1, res+")", result)
        generate_parenthesis(n, n, "", result)
        return result

    def generateParenthesis(self, n):
        res = []
        def helper(left, right, cur):
            if right == 0:
                res.append(cur)
                return
            if left > 0:
                helper(left - 1, right, cur + "(")
            if right > left:
                helper(left, right - 1, cur + ")")
        helper(n, n, "")
        return res



if __name__ == '__main__':
    test = Solution()
    print(test.generateParenthesis(3))

