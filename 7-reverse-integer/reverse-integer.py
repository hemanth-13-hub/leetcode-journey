class Solution:
    def reverse(self, x: int) -> int:
        b = str(abs(x))
        c = b[::-1]
        if c[0] == "0":
            c = int(c)
        else:
            c = int(c)
        if x < 0:
            c = -c
        if c < -2**31 or c > 2**31 - 1:
            return 0
        return c
        