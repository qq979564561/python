__builtins__.end = None

'''
adj="lovely"
name="Rabbits"
print("{} are {} animal".format(name,adj))

print("{0:.3f}".format(1.0/3))

print("{0:*^11}".format("Hello"))

print("{name:*^10} is best in the {where}".format(name='PHP',where='world'))
'''

'''print("a",end='')
print("b",end='')
print("c\n")
'''

'''
print('What\'s your name?')
print('The file is in D\\')
print("This is first line\nThis is second line")
print("The line will\
not the end") #this line == print("The line will not the end")
print(r"The \" is \\ a \t row \n line")
'''

'''
����='Hello'
print(����)
_1ver="World"
print(_1ver)
'''

'''
s="This is a long string.\
This continues the string.\
This is called ��ʾ������\
(Explict Line Joining)"
print(s)
'''

'''
str_1='a'
str_2='b'
num_1=3
num_2=6
num_3=0
num_4=1
print(str_1+str_2)
#print(str_1-str_2) has no meaning
print(str_1*3+str_2*3)
print(num_1**3)
print(num_3>>2)
print(num_4<<2)
print(not 0)
print(1 or 0)
'''

'''
a=3
a**=3
print(a)
'''

'''
print("Please Enter The Interger:")
right_number=23
guess=int(input())
    if guess==right_number:
        print("Congratulations! You guess right!")
    elif guess>right_number:
        print("No, its a little higher than it!")
    else:
        print("No, its a little lower than it!")
print("{string:*^10}".format(string="END"))
'''

'''
import sys
print("The command line arguments are:")
for i in sys.argv:
    print(i)

print("\n\nThe PythonPath is",sys.path,"\n")
'''

'''
import math
print("Enter num:")
num=int(input())
print("The square root is:",math.sqrt(num))

import os
print(os.getcwd)
'''

'''
from math import sqrt
print("Enter num:")
num=int(input())
print("The square root is\
{number:*^99}:".format(number=sqrt(num)))
'''

'''
import math
print("---Enter age and number---")
age=int(input("Age:"))
number=int(input("Number:"))
print("\nWhen its INT")
print("Number is {1:*^10}\nAge    is {0:*^10} \
".format(math.sqrt(age),math.sqrt(number)))
print("\nWhen its Float")
age=float(age)
number=float(number)
print("Number is {1:*^10}\nAge    is {0:*^10} \
".format(math.sqrt(age),math.sqrt(number)))
print("\nWhen its Complex")
'''

'''
import math
from math import sqrt
print("Enter what you want:")
judge=bool(input())
if judge:
    print("The square is {0:*^20}".format(sqrt(judge)))
'''

'''
import math
complex_number=complex(input())
print("{0:*^20}".format(math.sqrt(complex_number)))
'''

'''
import cmath
a=2
print(cmath.sqrt(a))
'''

'''
这是和同一文件夹下的test2.py文件一起的main测试程序1
import test0
test0.main()
'''

'''
import math as mt
print("{0}".format(mt.sqrt(16)))
'''

'''
animal=["cat","dog","rabbit","monkey","Godzilla"]
print("Enter the uncommon animals:")
rkey=5
while(1):
    animal_add=input()
    key=1
    for i in range(0,rkey):   #== for(i；i<rkey;i++)
        if animal_add==animal[i]:
            print("Its common!")
            key=0
            break
    print("\nThe final list is :")
    if key:
        animal.insert(rkey,animal_add)
        rkey=rkey+1
        for i in range(0,rkey):
            print(animal[i],end=" ")
    else:
        for i in range(0,rkey):
            print(animal[i],end=" ")
    print("\nEnter the uncommon animals:")
#animal[rkey]=animal_add 不能直接对界外位置的列表元素赋值,要用方法
'''

'''
animal_0=["cat","dog","rabbit","monkey","Godzilla"]
animal_1=["shark","lion","elephant","kangaroo","bird"]
#animal_0.extend(animal_1)
animal_0.extend(animal_1)
for i in range(0,10):
    print(animal_0[i])
'''

'''
animal_0=["cat","dog","rabbit","monkey","Godzilla"]
animal_0.extend(["lion"])
for i in range(0,6):
    print(animal_0[i])
'''

'''
animal=["cat","dog","rabbit"]
del animal[0]
print(animal)
'''

'''
animal=["cat","dog","rabbit"]
delete_animal=animal.pop(0)
print(delete_animal)
'''

'''
animal=["cat","dog","rabbit"]
delete_animal=animal.remove("cat")
print(delete_animal)
'''

'''
animal=["a","c","b"]
print("Original list:",animal)
animal.sort()
print("Using .sort()")
print(animal)
animal.sort(reverse=True)
print("Using .sort(reserve=True)")
print(animal)
print("Using sorted()")
print(sorted(animal))
print(len(animal))
print(animal.index("b"))
'''

'''
old_zoo=("dog","cat","monkey")
new_zoo=("python","penguin","elephant",old_zoo)
print("The old zoo list ",old_zoo)
print("The new zoo list ",new_zoo)
print("The old zoo\'s last animal is ",new_zoo[3][2])
for i in range(0,3):
    print("The old zoo has {animal}".format(animal=new_zoo[3][i]).title())
'''

'''
dictionary1={
"animal0":"cat",
"animal1":"dog",
"animal2":"lion",
"animal3":"monkey"
}
max_dic=4
#key_dic="animal0"
for i in range(0,max_dic):
    if i<max_dic:
        key_dic="animal"+str(i)
    print("The {0}th animal\'s name is:{1}".format(i,dictionary1[key_dic]))
    print(key_dic)
#为什么animal1键值反倒能调用字典里key为animal0的值？
'''

'''
dictionary1={
"animal0":"cat",
"animal1":"dog",
"animal2":"lion",
"animal3":"monkey"
}
max_dic=4
key_dic="animal0"
for i in range(0,max_dic):
    print("The {0}th animal\'s name is:{1}".format(i,dictionary1[key_dic]))
    print(key_dic)
    if i<max_dic:
        key_dic="animal"+str(i+1)
'''

'''
dictionary1={
"animal0":"cat",
"animal1":"dog",
"animal2":"lion",
"animal3":"monkey"
}
dictionary1["animal4"]=dictionary1
print(dictionary1["animal4"])
dictionary1[1+2j]="tiger"
print(dictionary1[1+2j])
dictionary1[("nihao")]="Hello"
print(dictionary1[("nihao")])
#dictionary1[["nihao"]]="Hello" #列表不可用做键值
#print(dictionary1[["nihao"]])
'''

'''
a=int(input())
print("The type is :",type(a))
'''

'''
string_test=0
print(str(string_test))
'''

'''
#It's wrong
dictionary1={
"animal0":"cat",
"animal1":"dog",
"animal2":"lion",
"animal3":"monkey"
}
for i in range(0,5):
    print(dictionary1[i])
'''

'''
list_section_test=["cat","dog","python","shark","monkey","Godzilla"]
print(list_section_test[0:6:2])
print(list_section_test[-2::-1])
print(list_section_test[:6:2])
print(list_section_test[::-2])
print(list_section_test[:])
list_section_test2=list_section_test[:]
print(list_section_test2)
'''

'''
list_set_test=['a','c','b']
list_set_test=set(list_set_test)
print(list_set_test)
'''

'''
list_set_test=['a','c','b']
list_set_test2=list_set_test
print(list_set_test)
del(list_set_test[0])
print(list_set_test2)
'''

'''
list_set_test=['a','c','b']
list_set_test2=list_set_test[:]
print(list_set_test)
del(list_set_test[0])
print(list_set_test2)
'''

'''
x=100
def fun():
    global x
    x=1
    print(x)
fun()
print(x)
'''

'''
def Outer():
    a=10
    def Inder():
        a=1
        print(a)
        def Inder2():
            nonlocal a
            a=10086
        Inder2()
        print(a)
    Inder()
    print(a)
Outer()
'''

'''
def fun ():
    print("Hello")
dic1={"key0":fun()}
dic1["key0"]
'''

'''
dic2={"key0":"index0","key1":"index1","key2":"index2"}
for i in range(0,3):
    print(dic2["key"+str(i)])
'''

'''
def fun_animal_print():
    animals=["cat","tiger","dog","shark","godzilla"]
    for animal in animals:
        print(animal.title())
        print("I like {0} so much".format(animal))
        print("But {0} is\' not my favourite\n".format(animal.title()))
        if __name__ == "__main__":
            print("I like python so much!")
fun_animal_print()
'''

'''
import test0
test0.fun_animal_print()
'''

'''
squares=[]
for value in range(1,11,1):
    square=value**2
    squares.append(square)
for i in range(0,len(squares)):
    print(squares[i],end=" ")
    if i==(len(squares)-1):
        print("\n")
#The first way
list=list(range(1,11,1))
for i in range(0,len(list)):
    print(list[i]**2,end=" ")
    if i==len(list)-1:
        print("\n")
#The second way
list_analysis=[value**2 for value in range(1,11,1)]
for i in range(0,len(list_analysis)):
    print(list_analysis[i],end=" ")
#The third way (列表解析)
'''

#以下为列表解析的练习
'''
list_even_numb=[even_numb for even_numb in range(1,101) if even_numb%2==0]
for i in range(0,len(list_even_numb)):
    print(list_even_numb[i],end="_")
'''
#normal code 1:
'''
text="My favourite language is Python"
list_first_chart=[]
for word in text.split():
    list_first_chart.append(word[0])
for i in range(0,len(list_first_chart)):
    print(list_first_chart[i],end=" ")
    if i == len(list_first_chart)-1:
        print("\n")
#list list analysis 1:
text="My favourite language is Python"
list_first_chart_2=[word[0] for word in text.split()]
for i in range(0,len(list_first_chart_2)):
    print(list_first_chart_2[i],end=" ")
    if i == len(list_first_chart_2):
        print("\n")
'''
#list analysis 2:
'''
a=[1,2,3,4]
b=[5,6,7,8]
list_combine=[i*j for i,j in zip(a,b)]
print(list_combine)
#for i in range(0,len(list_combine)):
#    print(list_combine[i],end=" ")
'''

'''
a=[1,2,3,4]
b=[5,6,7,8]
c=['a','b','c','d']
print(zip(a,b,c))
for i in zip(a,b,c):
    print(i)
'''

'''
a=[1,2,3,4]
b=['a','b','c','d','d','e']
c=["Nihao","Hello","Bonjour"] #此为最短序列
print(list(zip(a,b,c)))
'''

'''
list_2=[[1,2,3],[4,5,6],[7,8,9]]
print([[j[i] for j in list_2] for i in range(len(list_2[0]))])
print(list(zip[*list_2]))
'''

'''
days=['Monday','Tuesday','Wednesday']
fruits=['Apple','Banana','Pear']
drinks=['Tea','Juice','Coke']
list_diet=list(zip(days,fruits,drinks))
print(list_diet)
'''
'''
for day,fruit,drink in zip(days,fruits,drinks):
    print("{0:*^10}  Eat{1:*^10}  Drink{2:*^10}".format(day,fruit,drink))
'''

'''
list_ifelse=['1','2','3','4','5','o','6']
list_ifelse2=[int(i) if str(i).isdigit() else None for i in list_ifelse]
print(list_ifelse2)
'''

'''
import test0
a=int(input("Pleas intput a&b\n"))
b=int(input())
print("The value of a add b is:{:*^10}".format(test0.fun_add(a,b)))
'''


'''
import sys
list_iter=['a',2,"Helllo","___"]
it=iter(list_iter)
for value in it:
    print(value,end=" ")
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
'''

'''
a=3
b=4
a,b=b,a+b
print(a,b)
'''

'''
list_inter2=[1,2,3,4]
print(iter(list_inter2))
it=iter(list_inter2)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it)) #此行输出时会遇到StopIterration异常而结束
'''

'''
import sys
list_inter3=[1,2,3,4,5]
it0=list_inter3
for date0 in it0:
    print("{:>8}".format(date0))
it1=iter(list_inter3)
print("----------------")
for date1 in it1:
    print("{:>8}".format(date1))
'''

'''
a="test"
print("{0:>8}".format(a))
print("{0:^8}".format(a))
print("{0:*^8}".format(a))
'''

'''
a=13
print("{0:b}".format(a))
print("{0:d}".format(a))
print("{0:o}".format(a))
print("{0:x}".format(a))
'''
'''
print("{0:,}".format(123456789))
print("{0:.3f}".format(31.245567348))
'''

'''
list_temp=[1,2,3,4]
tuple_temp=('a','b','c','d')
dict_temp={"key0":"Nihao","key1":"Hello","key2":"Bonjour"}
def fun_temp():
    print("Test")
def print_info(monkey,*charts):
    print("输出part1:")
    print(monkey+'\n')
    #if charts:
    print("输出part2:")
    for date in charts:
        print("此时对象类型为：",end="")
        print(type(date))
        print(date)
list_temp_iter=iter(list_temp)
print(print_info("SRH","nihao",2018426,list_temp,tuple_temp,dict_temp,fun_temp,list_temp_iter))
'''

'''
You=True
def Love():
    if You:
        Love()
'''
'''
#x=(y=1)
x=1;y=2
print("Hello",x,y)
'''



'''
dict_traversal={
    "jen":"python",
    "jack":"ruby",
    "tom":"c",
    "outman":"c++",
    "Toky":"Python",
}
dict_traversal_2={
    'a':"nihao",
    'c':"Hello",
    'b':"Bonjour",
    'd':"Hello"
}
'''

'''
for name,language in dict_traversal.items():
    print(name.title()+
    "'s favourite language is "+
    language.title()+'!')
    print("\n{0:>8}'s favourite language is {1:*^8}\n"
    .format(name.title(),language.title()))
'''
'''
for date in set(dict_traversal_2.values()):
    print(date)
'''


'''
count=0
list_alien_first=[]
for i in range(0,30):
    dict_alien={"color":"green","point":5,"speed":"slow"}
    list_alien_first.append(dict_alien)
#以上是对包含字典的列表的创建
'''
'''
for i in range(0,30):
    print("\n")
    print(list_alien_first[i])
    count=count+1
print("\nThe total number is {0}".format(count))
'''
'''
#以上是对包含所有字典的完整列表的输出
for alien in list_alien_first[:3]:
    alien["color"]="yellow"
    alien["point"]="10"
    alien["speed"]="medium"
for alien in list_alien_first[:3]:
    print("\n")
    print(alien)
print("是否全面升级？(Y/N)")
judge=input()
if ((judge=='Y')or(judge=='y')):
    for alien in list_alien_first:
        if  "green"==alien["color"]:
            alien["color"]="yellow"
            alien["point"]="10"
            alien["speed"]="medium"
        elif "yellow"==alien["color"]:
            alien["color"]="red"
            alien["point"]="15"
            alien["speed"]="quick"
#以上是对列表中部分字典的单独修改
for i in range(0,30):
    print("\n")
    print(list_alien_first[i])
'''


'''
dic_list={
    "jake":["python","ruby"],
    "tom":["c++","java"],
    "outman":["haskell","PHP"],
    "peiqi":["html"]
}
for name,languages in dic_list.items():
    if len(languages) > 1:
        print("\n"+name.title()+"'s favourite languages are:",end=" ")
    else:
        print("\n"+name.title()+"'s favourite languages is:",end=" ")
        for language in languages:
            if language != "PHP":
                print(language.title(),end=" ")
            else:
                print(language.upper(),end=" ")
'''
#以上是对字典包含列表的练习

'''
dic_dic={
    "toky":{
        "first":"toky",
        "last":"shi",
        "location":"jinhua",
    },
    "tom":{
        "first":"tom",
        "last":"braun",
        "location":"german",
    }
}
#for dic in dic_dic:
for user,date in dic_dic.items():
    print("\n"+"\t"+"Username:",end=" ")
    print(date["first"].title(),end=" ")
    print(date["last"].title())
    print("\t"+"Location:",end=" ")
    print(date["location"].title())
'''
'''
n=int(input())
print("{0:-^20}".format(n*n))
'''
'''
n=int(input())
add_n=abs(n)+10
sub_n=abs(n)-10
mul_n=abs(n)*10
if n>=0:
    add_n=abs(add_n)
    sub_n=abs(sub_n)
    mul_n=abs(mul_n)
else:
    add_n=-abs(add_n)
    sub_n=-abs(sub_n)
    mul_n=-abs(mul_n)
print(abs(n),add_n,sub_n,mul_n)
'''
'''
n=float(input())
sum_good=1.0
sum_bad=1.0
for i in range(0,365):
    sum_good=sum_good*(1+n/1000)
    sum_bad=sum_bad*(1-n/1000)
print("{0:.2f},{1:.2f},{2:}".format(sum_good,sum_bad,int(sum_good/sum_bad)))
'''
'''
n=int(input())
for i in range(1,n+1,2):
    print("{0:^{1:}}".format('*'*i,n))
'''
'''
list_original_text=list(input())
list_nomal_text=list("abcdefghijklmnopqrstuvwxyz")
list_cipher_text=list("defghijklmnopqrstuvwxyzabc")
for org in list_original_text:
    location_1=list_original_text.index(org)
    for nomal in list_nomal_text:
        if org==nomal:
            location_2=list_nomal_text.index(nomal)
            list_original_text[location_1]=list_cipher_text[location_2]
for date in list_original_text:
    print(date,end="")
'''
'''
list_original_text=list(input())
list_nomal_text=list("abcdefghijklmnopqrstuvwxyz")
list_cipher_text=list("defghijklmnopqrstuvwxyzabc")
length=len(list_original_text)
for i in range(length096):
    for j in range(len(list_cipher_text)):
        if list_original_text[i]==list_cipher_text[j]:
            if j>=23:
                j=j-23

            if j<23:
                j=j+3
                list_original_text[i]=list_cipher_text[j]
for date in list_original_text:
    print(date,end="")
'''
'''
class Person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print('Hello, My name is {0:}'.format(self.name.title()))
p=Person('toky')
p.say_hi()
'''

'''
import sys
class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+"is now stitting")
    def roll(self):
        print(self.name.title()+"rolled over!")
    def dance(self):
        f=open("dance.txt")
        line=f.readline()
        while line:
            print(line,end="")
            line=f.readline()
        f.close()
my_dog=Dog('lulu',4)
print('My dog is '+my_dog.name+'.')
print('My dog is '+str(my_dog.age)+' years old.')
my_dog.dance()
'''

'''
class Dog():
    def __init__(self,dog_name,dog_age):
        self.name=dog_name
        self.age=dog_age
    def describe_dog(self):
        print("My dog is {0:}, it's {1:} years old!".format(self.name.title(),self.age))
dog=Dog("toky","18")
print("Describe my dog ? Press any key")
a=input()
if a or not a:
    dog.describe_dog()
'''


'''
class Restaurant():
        #在以下的init方法中初始化了(对象的)属性name和type
    def __init__(self,restaurant_name,cuisine_type):
        self.name_it=restaurant_name
        self.type_it=cuisine_type
        #在以下的describe_restaurant方法中输出了对象的name和type属性
    def describe_restaurant(self):
        print("{0:<10}, the cuisine type is {1:}".format(self.name_it,self.type_it))
        #在以下的open_restaurant方法中输出了对象的name和type属性
    def open_restaurant(self):
        print("The {0:} is opening!".format(self.name_it))
mc=Restaurant("Mcdownload","humbergers")
kfc=Restaurant("KFC","chips")
sb=Restaurant("Starbucks","coffee")
print("Please input the New restaurant's name and the cuisine:")
name_restaurant_input=input()
cuisine_type_input=input()
new_restaurant=Restaurant(name_restaurant_input,cuisine_type_input)
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
print("{0:*^45}".format("*"))
print("The old restaurant are:")
mc.describe_restaurant()
kfc.describe_restaurant()
sb.describe_restaurant()
'''
'''
name_test="monkey"
class Test_class():
    def __init__(it,name_test,number_test):
        name=name_test
        number=number_test
    def print_it(it):
        print(it.name,it.number)
        #此时会报错，上面的name和number只是局部变量，如果使用了it，此时it指实例本身，
        #因此it.name,it.number修改（初始化赋值）的就是全局变量,在类中使用句号表示发即可通用。
        #注意，此处只是为了更清楚地表达 代表实例本身的形参变量的实质，采用it，通常约定为self
test=Test_class("toky","20")
test.print_it()
'''

'''
class Test_class():
    def test_1(self,name_test,number_test):
        self.name=name_test
        self.number=number_test
    def print_it(self):
        print(self.name,self.number)
test=Test_class("toky","20")
test.print_it()
'''

'''
class Dog_test():
    def __init__(self,name_dog,age_dog):
        self.name=name_dog
        self.age=age_dog
        self.sex="boy" #给属性指定默认值
    def print_dog(self):
        print("The name of the dog is: {0:}".format(self.name.title()))
        print("The age of it is: {0:}".format(self.age))
    def add_age(self,add_number):
        if add_number>=0:
            self.age=self.age+add_number
        else:
            print("The add number is not legal !")
dog_test=Dog_test("alex",13)
print("{0:-^40}".format("The former info of the dog:"))
dog_test.print_dog()
print("{0:-^40}".format("How many years passed?"))
years_passed=int(input())
dog_test.add_age(years_passed)
print("{0:-^40}".format("Now the dog info:"))
dog_test.print_dog()
'''

#以下是对类的练习，重要！

'''
class Super_dog():
    def __init__(self,name_dog,age_dog):
        self.name=name_dog
        self.age=age_dog
        self.sex="boy" #给属性指定默认值
    def print_dog(self):
        print("The name of the dog is: {0:}".format(self.name.title()))
        print("The age of it is: {0:}".format(self.age))
    def add_age(self,add_number):
        if add_number>=0:
            self.age=self.age+add_number
        else:
            print("The add number is not legal !")
    def print_special(self):
        print(self.sex)

class Figure():
    def __init__(self,height=50,width=80):
        self.height=height
        self.width=width
    def print_figure(self):
        print("The height is {0:}".format(self.height))
        print("The width is {0:}".format(self.width))

class Dog_son(Super_dog):   #括号内必须包含父类的名称#
    def __init__(self,name_dog,age_dog):    #初始化父类（超类）的属性#
        super().__init__(name_dog,age_dog)
        self.power=80
        self.figure=Figure()
    def print_power(self):
        print(self.power)
    def print_special(self):
        print("It's changed")

dog_son=Dog_son("alex",3)
dog_son.print_dog()
dog_son.print_power()
dog_son.print_special()
dog_son.figure.print_figure()

from Dog_class import Dog_son
mydog=Dog_son("toky",18)
mydog.print_dog()
'''
#以上是对类的练习，重要！

'''
with open('pi_digits.txt') as file_object: #关键字with在不需要访问文件后将其关闭
    contents=file_object.read()
    print(contents.rstrip())
#使用上述with内的结构，可以让python去确定：需要时调用，在合适的时候关闭
'''
'''
file_path=r"text\你好世界.txt"
with open(file_path) as file_object:
    contents=file_object.read()
    print(contents)
'''
'''
file_name="pi_million_digits.txt"
with open(file_name)as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string=pi_string+line.strip()   #strip()   lstrip()    rstrip()
print(pi_string[0:52:1]+"...")
print(len(pi_string))
print("{0:}".format('-'*52))
your_name=input("Enter your birthday,see if is in the pi:\n")
if your_name in pi_string:
    print("Its in!")
else:
    print("Not in ")
'''


#以下是对异常处理的练习#
#1.统计文件字数的函数
'''
def num_word(filename):
    try:
        with open(filename)as object_file:
            contens=object_file.read()
            word_list=contens.split()
    except FileNotFoundError:
        error_msg="sorry, there is not such file!"
        print(error_msg.title())
    else:
        print(word_list)
        print("There are {0:} words in book")
filename=r'text\siddhartha.txt'
num_word(filename)
'''
#10-6
'''
list_number=[]
print("Please input the number to add:")
def number_enter_check():
    try:
        for i in range(0,2):
            list_number[i]=int(input())
    except ValueError:
        print("Sorry, you enter the string, try again!")
    else:
        print("The sum is {0:}".format(list_number[0]+list_number[1]))
number_enter_check()
'''
#函数——读取并打印文件文本内容
'''
def print_contents(file_name="AKA.txt"):
    try:
        with open(file_name,'r')as file_object:
            contents=file_object.read()
    except:
        print("No such file!")
    else:
        print(contents)
'''
#对文件写入模式的练习
'''
def prc_file_write(msg_write,file_name=r"text\prc_file_write.txt"):
    try:
        with open(file_name,'w')as file_object:    #使用'w'写入模式，会在返回文件对象前清空该文件
            file_object.write(msg_write)
    except FileNotFoundError:
        pass
    else:
        print("Write Success!")

msg_write=input("Write the message:\n")
prc_file_write(msg_write)
print("{0:}".format('-'*30))
print("Output the message:")
print_contents(file_name="text\prc_file_write.txt")
'''

#对文件附加模式的练习
'''
def prc_file_add(msg_add,file_name=r"text\prc_file_add.txt"):
    try:
        with open(file_name,'a')as object_file:
            object_file.write(msg_add)
    except FileNotFoundError:
        print("There is not such file")
    else:
        print("Add Success")
msg_add=input("Add the message:\n")
prc_file_add(msg_add)
print("{0:}".format('-'*30))
print_contents(file_name="text\prc_file_add.txt")
'''
'''
#对文件读取和写入模式r+的练习
def prc_file_r_plus(msg_r_plus,file_name=r"text\prc_file_r_plus.txt"):
    try:
        with open(file_name,'r+')as object_file:
            object_file.write(msg_r_plus)
    except FileNotFoundError:
        print("error")
    else:
        object_file.close()
        print("Write Success")

def prc_file_r_plus_out(file_name=r"text\prc_file_r_plus.txt"):
    try:
        with open(file_name,'r+')as object_file:
            contents=object_file.read()
    except FileNotFoundError:
        print("error")
    else:
        print(contents)

msg_r_plus=input("Write the message:\n")
prc_file_r_plus(msg_r_plus)
print("{0:}".format('-'*30))
print("Output the message:")
prc_file_r_plus_out()

#相关blog:   https://www.cnblogs.com/Justice-V/articles/8099056.html
'''



'''
a=1
c=2
def fun(b):
    return b+1
a=fun(a)
c=fun(c)
print(a,c)
'''

'''
#list
list_1=[1,2,3]
def fun_list(list):
    list[0]=2333
fun_list(list_1)
print(list_1)
#vx
a=1
def fun_vx(b):
    b=2333
fun_vx(a)
print(a)
#python
'''

'''
#以下是对使用json模块进行数据储存与输出的练习
import json
filename='number_new.jason'
numbers=input("Enter any numbers you want\n")
print("{0:}".format('-'*30))
def dump_fun(filename):
    try:
        with open(filename,'w') as obj_file:
            json.dump(numbers,obj_file)
    except FileNotFoundError:
        json.dump(numbers,obj_file)
        print("No such file, but we will create it")
        print("{0:}".format('-'*30))
    else:
        print("Write Success!")
def load_fun(filename):
    try:
        with open(filename) as obj_file:
            vex=json.load(obj_file)
    except FileNotFoundError:
        print("No such file!")
    else:
        print("{0:}".format('-'*30))
        print("Open Success!")
        print("{0:}".format('-'*30))
        number=vex
        print(number)
dump_fun(filename)
load_fun(filename)
print(numbers)
'''

'''
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
'''
'''
import json
filename="username.json"
try:
    with open(filename) as obj_file:
        username = json.load(obj_file)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename,'w') as obj_file:
        json.dump(username,obj_file)
        print("We'll remember you when you come back," + username + "!")
else:
    print("Welcome back," + username + "!")
'''
'''
import json
def prc_json(filename):
    try:
        with open(filename) as obj_file:
            username = json.load(obj_file)
    except FileNotFoundError:
        username=input("What's your name ? ")
        with open(filename,'w') as obj_file:
            json.dump(username,obj_file)
            print("We'll remember you when you come back," + username + "!")
    else:
        print("Welcome back," + username + "!")

filename="prc_json.json"
prc_json(filename)
'''

'''
import os
print("Hello")
key=input()
os.system("cls")
'''

'''
#以下是对函数测试代码的练习
import unittest
from prc_import_case import full_name
#first_name=input("Please enter your first name:\n")
#last_name=input("Please enter your last name:\n")
#full_name(first_name,last_name)
class FullNameTest(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name_0=full_name("toky","sama")
        self.assertEqual(formatted_name_0,"Toky Sama")
    def test_first_last_mid_name(self):
        formatted_name_1=full_name("toky","sama","happy")
        self.assertEqual(formatted_name_1,"Toky Happy Sama")
unittest.main()
'''

#11-3
'''
class Employee():
    def __init__(self,first_name,last_name,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
    def add_salary(self,add_salary=5000):
        self.salary+=add_salary
    def print_name_salary(self):
        name=self.first_name + ' ' +self.last_name
        print("\nThe {0:} 's salary is {1:{2:}^20}".format(name.title(),str(self.salary),'*'))
staff_jack=Employee("jack","london",5000)
staff_jack.add_salary()
staff_jack.print_name_salary()
'''
'''
#11-3
import unittest
from prc_import_case import Employee
class staff_class_prc(unittest.TestCase):
    def setUp(self):
        self.jack=Employee("jack","london",65000)
    def test_give_default_raise(self):
        self.jack.add_salary()
        self.assertEqual(self.jack.salary,70000)
    def test_give_custom_raise(self):
        self.jack.add_salary(10000)
        self.assertEqual(self.jack.salary,75000)
unittest.main()
'''

'''
import random
vex_a=random.random()
vex_b=random.randint(1,100)
vex_c=random.uniform(10,20)
print(vex_a,vex_b,vex_c,sep="\n")
'''

'''
#异常处理中的finally
try:
    a=int(input("Please endter what you want: "))
    sum=10086/a
except ZeroDivisionError:
    print("hhh")
else:
    print(sum)
finally:
    print("\nTest Over!\n")
'''

'''
#random中的seed (同c/c++,是伪随机)
#不必特地地去设置，python会帮你选择seed
import random
import time
random.seed(10)
print("Random number with 10 is:",random.random())
random.seed(10)
print("Random number with 10 is:",random.random())
random.seed(10)
print("Random number with 10 is:",random.random())
random.seed(10)
print("Random number with 10 is:",random.random())
#以上，同一个seed生成的随机数始终相同
print("{0:}".format('-'*45))
random.seed(time.time())
print("Random number with time is:",random.random())
'''
'''
import random
single=random.random()
list=random.randint(1,2)
print(single)
print(list)
'''
'''
######
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
'''
list_builder=[x*x for x in range(1,10) if x*x/2 != 0]
print(list_builder)
'''
#print("Hello World!")




#####################################
#数据结构与算法#
'''
#冒泡排序#
import time
import random

#开始时间
first_time = time.time()

def new_num(num_list):
    """随机生成50个数"""
    for i in range(50):
       j = random.randint(0, 100000)
       num_list.append(j)
    return num_list

def bubble_sort_high(num_list):
    """升序"""
    for i in range(len(num_list)-1, 0, -1):
        for j in range(i):
            if num_list[j+1] < num_list[j]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

def bubble_sort_low(num_list):
    """降序"""
    for i in range(len(num_list)-1, 0, -1):
        for j in range(i):
            if num_list[j+1] > num_list[j]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]



if __name__ == '__main__':
    num_list_high = []
    new_num(num_list_high)
    bubble_sort_high(num_list_high)
    print("###冒泡排序-升序{0:}".format("#"*100))
    print(num_list_high)

    num_list_low = []
    new_num(num_list_low)
    bubble_sort_low(num_list_low)
    print("###冒泡排序-降序{0:}".format("#"*100))
    print(num_list_low)

    last_time = time.time()
    print('共用时{0}'.format(first_time - last_time))
'''
#####################################

#####################################
#直接插入排序#
'''
import random
import time

def new_num(num_list):
    """随机生成50个数"""
    for i in range(50):
       j = random.randint(0, 100000)
       num_list.append(j)
    return num_list

def insert_direct_sort(num_list):
    n = len(num_list)
    #从第二个位置 开始插入 坐标为 1
    for i in range(1,n):
    #从第 i 个数开始比较（即从前往后），如果小于前一个数，则插入（交换位置）
        for j in range(i,0,-1):
            if num_list[j] < num_list[j-1]:
                num_list[j], num_list[j-1] = num_list[j-1], num_list[j]

if __name__ == '__main__':
    num_list = []
    new_num(num_list)
    insert_direct_sort(num_list)
    print("###插入排序-升序{0:}".format("#"*100))
    print(num_list)
'''
#####################################

#####################################
#希尔排序 （重构直接插入排序实现）#
'''
import time
import random

def shell_insert_sort(array, len_array, dk):
    """直接插入排序"""
    # dk 为增量
    for i in range(dk, len_array):
        position = i
        current_value = array[position]

        index = 1
        j = int(index / dk)
        # j 为index与dk的商
        index = index - j * dk
        # index为下标
        while position > index and current_value < array[position - dk]:
            # 当前数要小于序列值时为升序
            # 后移
            array[position] = array[position -dk]
            position = position -dk
        else:
            array[position] = current_value

def shell_sort(array, len_array):
    """希尔排序"""
    dk = int(len_array / 2)
    # dk 为增量，增量大于等于 1
    while(dk >= 1):
        shell_insert_sort(array, len_array, dk)
        print("当增量为{0:}时".format(dk),end = ",")
        print("Shell: ",array)
        dk = int(dk / 2)

def new_num(num_list):
    """随机生成数(大小10k以内)"""
    for i in range(5):
       j = random.randint(0, 100000)
       num_list.append(j)
    return num_list

if __name__ == "__main__":
    num_list = []
    new_num(num_list)
    print("Original: ",num_list)
    shell_sort(num_list, len(num_list))
'''
#####################################

#####################################
'''
#快速排序
import random
import time

def quik_sort(array, left, right):
    if left < right:
        q = partition(array, left, right)
        quik_sort(array, left, q - 1)
        quik_sort(array, q + 1, right)

def partition(array, left, right):
    """以枢纽 pivotkey 为中心，分割关键字序列，且分别进行排序"""
    x = array[right]
    #x = array[left]
    i = left -1
    for j in range(left, right):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1

def new_num(num_list):
    """随机生成数(大小10k以内)"""
    for i in range(500):
       j = random.randint(0, 100000)
       num_list.append(j)
    return num_list

if __name__ == "__main__":
    num_list = []
    new_num(num_list)
    quik_sort(num_list, 0, len(num_list)-1)
    quik_sort(num_list, 0, len(num_list)-1)
    quik_sort(num_list, 0, len(num_list)-1)
    print(num_list)
#####################################
'''

#####################################

import  matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()
