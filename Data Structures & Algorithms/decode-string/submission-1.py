class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i]==']':
                subs = ""
                while stack and stack[-1]!='[':
                    subs = stack.pop()+subs
                stack.pop()
                l = ""
                while stack and stack[-1].isdigit():
                    l = stack.pop()+l
                stack.append(int(l)*subs)
            else:
                stack.append(s[i])
        
        return "".join(stack)
                

            