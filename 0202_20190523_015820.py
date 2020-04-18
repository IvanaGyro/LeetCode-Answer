class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            n = sum((ord(s)-ord('0'))**2 for s in str(n))
        return True
    