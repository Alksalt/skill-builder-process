class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

    def addDigits(self, num: int) -> int:
        result = 0
        while num >= 10:
            result = 0
            while num > 0:
                result += num % 10
                num //= 10
            num = result
        return num

    def addDigits2(self, num: int) -> int:
        result = 0
        while num > 0 or result >= 10:
            if num == 0:
                num, result = result, 0
            result += num % 10
            num //= 10
        return result


if __name__ == "__main__":
    sol = Solution()

    # Example usage (fill expected after solving)
    print(sol.addDigits(38))        # expected: ?
    print(sol.addDigits(0))         # expected: ?
    print(sol.addDigits(123))       # expected: ?

    # Extra edge ideas
    print(sol.addDigits(9))         # already single digit
    print(sol.addDigits(9999))      # multiple reduction steps
    print(sol.addDigits(2147483647))  # max input
