class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i,item in enumerate(s):
            if item=='(':
                stack.append(i)
            elif item ==')':
                if stack and s[stack[-1]]=='(':
                    stack.pop()
                else:
                    stack.append(i)
        if not stack:
            return len(s)
        else:
            n = len(s)
            stack = [-1]+stack+[n]
            val = stack[1]-stack[0]-1
            #print(stack)
            for i in range(2,len(stack)):
                if stack[i]-stack[i-1]-1>val:
                    val = stack[i]-stack[i-1]-1
            return val
                
                