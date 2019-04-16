class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            if digits[~i] == 9:
                digits[~i] = 0
                carry = 1
            else:
                carry = 0
                digits[~i] += 1
                break
        if carry:
            digits.insert(0, 1)
        return digits