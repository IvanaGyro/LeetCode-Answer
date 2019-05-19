class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def version2list(ver):
            arr = list(map(int, ver.split('.')))
            while arr and arr[-1] == 0:
                arr.pop()
            return arr
        version1 = version2list(version1)
        version2 = version2list(version2)
        if version1 > version2:
            return 1
        elif version1 < version2:
            return -1
        else:
            return 0
        