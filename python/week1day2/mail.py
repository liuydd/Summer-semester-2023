import re
def mail(mail):
    pattern=r'^\w+@[A-Za-z0-9]+(\.[A-Za-z0-9]+)+$'   #这里后面需要括号再++
    if re.match(pattern,mail):
        return True
    else:
        return False

m=input()
if mail(m):
    print(True)
else:
    print(False)