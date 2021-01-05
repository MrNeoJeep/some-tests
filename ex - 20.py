#有效的括号  哈希表+辅助栈
s = '[(]'
dict = {'}':'{',']':'[',')':'('}

stack = []
for c in s:
    if c in dict:
        if not stack or stack[-1] != dict[c]:
            print('False')
        stack.pop()
    else:
        stack.append(c)
n = len(stack)
if n == 0:
    print('true')
else:
    print('false') 
