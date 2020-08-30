def basiccalculator(s):
    if not s:
        return 0
    num = 0
    stack = []
    sign = '+'
    for i in range(len(s)):
        if s[i].isdigit():
            num = num*10 + int(s[i])
        elif (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
            if sign =='-':
                stack.append(-num)
            elif sign =='+':
                stack.append(num)
            elif sign == '*':
                stack.append(stack.pop()*num)
            else:
                tmp = stack.pop()
                if tmp//num <0 and tmp%num !=0:
                    stack.append(tmp//num+1)
                else:
                    stack.append(tmp//num)
            sign = s[i]
            num =0
    return sum(stack)
s1 = " 3+5 / 2 "
print(basiccalculator(s1))
