class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        max_len = max(len(n) for n in nums)
        def get_key(n):
            diff = max_len-len(n)
            tmp = n + n[0]*diff
            tmp += tmp[diff:]
            return tmp
        
        nums.sort(key=get_key, reverse=True)
        res =  ''.join(nums)
        for c in res:
            if c != '0':
                break
        else:
            return '0'
        return res
    