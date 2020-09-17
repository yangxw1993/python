class Tool:
  count = 0
  # 类方法
  @classmethod
  def show_count(cls):
    print(f'count: {cls.count}')
  @staticmethod
  def name():
    print('这是一个工具')
  def __init__(self,name):
    Tool.count +=1
    self.name = name

tool1 = Tool('🪓🪓🪓🪓🪓')
tool2 = Tool('🔨🔨🔨🔨🔨')
Tool.show_count()
Tool.name()