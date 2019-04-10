class Solution:
    def simplifyPath(self, path: str) -> str:
        import os
        from pathlib import Path
        # dir_arr = path.split("/")
        # stack = []
        # for d in dir_arr:
        #     if d == "." or d == "":
        #         continue
        #     if d != "..":
        #         stack.append(d)
        #     else:
        #         if stack:
        #             stack.pop()
        # return "/" + "/".join(stack)
        top = "./data"
        for f in os.listdir(top):
            pathname = os.path.join(top, f)
            mode = os.stat(pathname).st_mode
            print(pathname, f"{mode:x}", os.path.isdir(pathname))
        # return os.path.realpath(path)
    