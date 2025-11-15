class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join(
            chr(asc | 32) if 65 <= (asc := ord(ch)) <= 90 else ch for ch in s   # := 是海象运算符，表示临时将值赋予asc，可以在计算表达式的同时，将结果赋予变量，是为了重复计算
        )

solution = Solution()
print(solution.toLowerCase("AJIJOJIOFNO"))