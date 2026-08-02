class Solution:
    def simplifyPath(self, path: str) -> str:
        sub = path.split("/")
        stack = []
        for s in sub:
            if s == "" or s == ".":
                continue
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        ans = ("/".join(stack))
        return ("/" + ans)
