class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []
        res = []
        
        def helper(offset, path):
            nonlocal s
            if len(s) - offset > (4 - len(path)) * 3:
                return
            elif len(s) - offset < 4 - len(path):
                return
            elif len(path) == 4:
                res.append('.'.join(path))
                return
            for i in range(offset, offset + 3):
                if i >= len(s):
                    return
                n_s = s[offset : i+1]
                if n_s[0] == '0' and len(n_s) != 1:
                    return
                n = int(n_s)
                if n > 255:
                    return
                helper(i+1, path + [n_s])
        helper(0, [])
        return res
            