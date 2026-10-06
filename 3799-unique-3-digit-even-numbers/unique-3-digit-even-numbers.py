class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s=set()
        n=len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!=j and i!=k and j!=k:
                        if digits[i]!=0 and digits[k]%2==0:
                            x=digits[i]*100+digits[j]*10+digits[k]
                            s.add(x)
        return len(s)

        