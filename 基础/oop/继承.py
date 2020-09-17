class Animal:
  def eat(self):
    print('吃')
  def drink(self):
    print('喝')


# 子类拥有父类的属性和方法
class Dog(Animal):
  def bark(self):
    print('汪汪汪')

class XiaoTianQuan(Dog):
  # 重写
  def bark(self):
    super().bark()
    print('我是神狗🐶')
  def fly(self):
    print('我会飞')
wangcai = Dog()
wangcai.eat()
xtq = XiaoTianQuan()
xtq.bark()