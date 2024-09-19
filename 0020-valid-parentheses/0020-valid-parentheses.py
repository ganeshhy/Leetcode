class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        
        stack=[0]
        for i in range(len(s)):
                if s[i]=='(':
                    stack.append("(")
                elif s[i]=="{":
                    stack.append("{")
                elif s[i]=="[":
                    stack.append("[")
                elif s[i]==")":
                    if stack[-1]=="(":
                        stack.pop()
                    else:
                        stack.append(")")
                        break
                elif s[i]=="}":
                    if stack[-1]=="{":
                        stack.pop()
                    else:
                        stack.append("}")
                        break
                elif s[i]=="]":
                    if stack[-1]=="[":
                        stack.pop()
                    else:
                        stack.append("]")
                        break
        if len(stack)==1:
            return 1
        else:
            return 0
            