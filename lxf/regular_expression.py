import re
'''
key=re.match(r'^\d{3}\s+\w{3}','123         abc')
if key:
    print('right')
else:
    print('no')
'''
print(re.split(r'\s+','a b    c'))
print(re.split(r'[\s\,\;]+','a,b,  c;1,2,   3'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0)) #Original string
print(m.group(1))
print(m.group(2))
