from collections import defaultdict, deque
class Solution:
     def findLadders(self, beginWord, endWord, wordList):
          if endWord not in wordList:
               return []
          d = defaultdict(list)
          for word in wordList:
               for i in range(len(word)):
                    d[f'{word[:i]}_{word[i+1:]}'].append(word)

          visited = deque([set((beginWord,))])
          res = deque([[beginWord]])

          for _ in range(len(wordList)):
               found = False
               masks = set()
               for i in range(len(res)):
                    path = res.popleft()
                    used = visited.popleft()
                    w = path[-1]
                    for i in range(len(w)):
                         mask = f'{w[:i]}_{w[i+1:]}'
                         if mask in d:
                             masks.add(mask)
                             for key in d[mask]:
                                  if key not in used:
                                       res.append(path + [key])
                                       visited.append(used | set((key,)))
                                  if key == endWord:
                                       found = True
               for mask in masks:
                   del d[mask]
               if found:
                   break
          return [path for path in res if path[-1] == endWord]

          
