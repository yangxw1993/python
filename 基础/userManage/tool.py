user_list = []
def show_menu():
  menus = ['欢迎使用名片管理系统', '1.新增名片', '2.显示名片', '3.搜索名片', '', '0.退出']
  print('*' * 50)
  for item in menus:
    print(item)
  print('*' * 50)
def print_header():
  for item in ['姓名', '电话', '城市']:
    print(item, end='\t\t\t')
def print_body(user_item):
  print('%s\t\t\t%s\t\t\t%s\t\t\t' % (user_item['name'], user_item['phone'], user_item['city']))
def show_all():
  print('-' * 10)
  print('showAll')
  if len(user_list) == 0:
    print('当前没有任何名片记录，请使用添加名片')
    return
  # 表头
  print_header()
  print('')
  for user_item in user_list:
    print_body(user_item)
  print('-' * 10)

def add_user():
  print('-' * 10)
  print('add')
  name = input('请输入姓名：')
  phone = input('请输入手机号：')
  city = input('请输入城市：')
  user_item = {
    'name': name,
    'phone':phone,
    'city':city
  }
  user_list.append(user_item)
  print_body(user_item)
  print(f'添加{name}的名片成功')
  print('-' * 10)

def search():
  print('-' * 10)
  print('search')
  query_name = input('请输入要搜索的姓名🔍：')
  for user_item in user_list:
    if(user_item['name'] == query_name):
      print_header()
      print_body(user_item)
      operate(user_item)
      break
  else:
    print('抱歉，没有找到%s'% query_name)
  print('-' * 10)

def operate(user_item):
  input_str = input('请选择要执行的操作：\n [1]修改 [2]删除 [0]返回上一级')
  if input_str == '1':
    user_item['name'] = edit_value('姓名',user_item['name'])
    user_item['phone'] = edit_value('手机',user_item['phone'])
    user_item['city'] = edit_value('城市',user_item['city'])
    print('修改名片成功')
  elif input_str == '2':
    user_list.remove(user_item)
    print('删除名片成功')

def edit_value(type, value):
  input_value = input(f'当前值为{value}请输入{type}(回车不修改):')
  if input_value:
    return input_value
  else :
    return value