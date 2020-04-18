from collections import defaultdict
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        T = lambda: defaultdict(T)
        char_dict = defaultdict(T)
        h, w = len(board), len(board[0])
        for word in words:
            n = char_dict
            for c in word:
                n = n[c]
            n['#'] = word
        
        res = []
        def dfs(y, x, node):
            save = board[y][x]
            if save in node:
                next_node = node[save]
                word = next_node.pop('#', False)
                if word:
                    res.append(word)
                board[y][x] = '_'
                for yd, xd in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    if 0 <= y+yd < h and 0 <= x+xd < w:
                        dfs(y+yd, x+xd, next_node)
                if not next_node:
                    node.pop(save)
                board[y][x] = save
            return 
        
        for y in range(h):
            for x in range(w):
                dfs(y, x, char_dict)
    
        return sorted(res)
    