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
