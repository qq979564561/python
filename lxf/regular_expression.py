import re
'''
key=re.match(r'^\d{3}\s+\w{3}','123         abc')
if key:
    print('right')
else:
    print('no')
'''
print(re.split(r'\s+','a b    c'))
