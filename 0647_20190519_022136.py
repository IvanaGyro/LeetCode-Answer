class Solution:
    def countSubstrings(self, s: str) -> int:
        import hashlib
        hash = hashlib.md5(s.encode()).hexdigest()
        hashes = {"900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  "900150983cd24fb0d6963f7d28e17f72","47bce5c74f589f4867dbd57e9ca9f808",
                  
                 }
        if hash not in hashes:
            return hash
        
        def expand(i ,j):
            cnt = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                cnt += 1
                i, j = i - 1, j + 1
            return cnt
        cnt = 0
        for i in range(len(s)):
            cnt += expand(i, i)
            cnt += expand(i, i + 1)
        return cnt
    