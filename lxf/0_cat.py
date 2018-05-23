import math




'''
print('你好'.encode('utf-8'))
print("Hi %s, you have %d dollars!"%('toky'.title(),10000))
#python中的%格式化方法: print("xxx %s xxx"%"xx")
print("Hi {0:}, you have {1:} dollars!".format("toky".title(),10000))
print('grow rate: %d %%'%7)
'''

#list=[1,2,3,4,5,]
#####
def check_range(list):
    try:
        index=int(input('Enter the index:\n'))
        print(list[index])
    except IndexError:
        print('Out of the range')
    else:
        print("\nSuccess!")
#####
'''
#check_range()
list_1=['a','b','c']
list_2=[1,2,3,list_1]
#print(list_2[3])
#check_range(list_2)
#print(list_2[3][0])
'''
'''
str_add=input('Add to list:\n')
list_2.append(str_add)
check_range(list_2)
'''
'''
tuple_1=(1,[1])
#当定义只有一个元素的元组时，要在1的后面加一个逗号，避免认为其为一个数字1的歧义
#tuple_1=[]
tuple_1[1][0]="nihao"
print(tuple_1[1][0])
'''
'''
list_1=[]
tuple_1=(1,list_1)
while True:
    vex=input()
    if vex == 'quit':
        break
    tuple_1[1].append(vex)
    print(list_1)
'''
'''
age = 20
if age >= 6:
    print('teenager')
if age >= 18:
    print('adult')
else:
    print('kid')
#if 语句从上往下判断，有一个if 为True后，自动忽略接下来的elif或else
'''

####
def equation_2(a,b,c):
    try:
        vex_a=math.fabs(math.sqrt((b**2-4*a*c)/(4*(a**2)))-b/(2*a))
        vex_b=-vex_a
    except (ValueError, TypeError):
        print("\nMath Domain Error")
        vex_a=vex_b=-1
        #return vex_a,vex_b
        return None
    else:
        return vex_a,vex_b
#####
'''
x,y=equation_2(9,1,4)
if x!=-1 and y!=-1:
    print(x,y)
'''
class Mywife():
    def __init__(self,name,type):
        self.name=name
        self.type=type
        self.age=0
    def print_info(self):
        print("\nMy wife {0:} is a {1:}".format(self.name.title(),self.type))
    def print_age(self):
        self.age=18
        print("\nHer age is {0}".format(self.age))
#####
'''
name_wife=input("Enter your wife's name: \n")
type_wife=input("Enter your wife's type: \n")
mywife=Mywife(name_wife,type_wife)
print("{0}".format('-'*35))
mywife.print_info()
mywife.print_age()
'''
'''
my_first_wife=Mywife("zz","cat")
print(isinstance(my_first_wife,Mywife))
list_is=[1,2,3,4,5]
print(isinstance(list_is,list))

print(dir(Mywife))
'''
list_builder=[x*x for x in range(1,10) if x*x/2 != 0]
print(list_builder)
list_1=['x','y','z']
list_2=[1,2,3]
list_combine=[vexa+' = '+str(vexb) for vexa in list_1 for vexb in list_2 ]
print(list_combine)
