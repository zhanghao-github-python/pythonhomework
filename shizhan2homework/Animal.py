# =================conding: utf-8
"""
================================================================================

Author : Administrator
Created  on : 2021/7/4
Project ： PyCharm
File  : Animal
E-mail: zh13997821732@163.com


================================================================================

"""


class Animal:
    name = ''
    color = ''
    age = ''
    gender = ''

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def cry(self):
        print(f'cry方法：颜色为:{self.color}的动物，名叫:{self.name}我会叫，年龄为:{self.age}岁,性别为:{self.gender}')

    def run(self):
        print(f'run方法：颜色为:{self.color}的动物，名叫:{self.name}会跑，年龄为:{self.age}岁,性别为:{self.gender}')
    # @classmethod
    # def class_cry(cls):
    #     print("动物会跑会叫")


class cat(Animal):

    def __init__(self, name, color, age, gender):
        self.hair = '短发'
        super().__init__(name, color, age, gender)

    def catch_mice(self):
        if self.age >= 1:
            print(f"我是一只{self.color}的{self.gender}猫，我叫{self.name},我今年{self.age}岁了，我的毛发是{self.hair}的，我今天抓到了老鼠")
        else:
            print('年龄小，抓不到老鼠~')

    def cry(self):
        print(f'cry方法：我的颜色为:{self.color}的动物，名叫:{self.name}我会一起喵喵叫，年龄为:{self.age}岁,性别为:{self.gender}')


class dog(Animal):
    def __init__(self, name, color, age, gender):
        self.hair = '长发'
        super().__init__(name, color, age, gender)

    def housekeeping(self):
        if self.age >= 1:
            print(f"我是一只{self.color}的{self.gender}狗，我叫{self.name},我今年{self.age}岁了，我的毛发是{self.hair}的，我今天在家独自看家护院")
        else:
            print("年龄过小，不能看家呢~")

    def cry(self):
        print(f'cry方法：颜色为:{self.color}的动物，名叫:{self.name}我会对陌生人汪汪叫，年龄为:{self.age}岁,性别为:{self.gender}')


if __name__ == '__main__':
    catlele = cat('乐乐', '蓝白', 1, '公')
    catlele.catch_mice()
    doglele = dog('小黑', '黑色', 2, '母')
    doglele.housekeeping()
