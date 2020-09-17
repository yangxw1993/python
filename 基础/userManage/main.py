#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import tool
while True:
  tool.show_menu()
  input_str = input('请选择要操作的序号:')
  print(f'您选择操作是', input_str)

  if input_str in ['1', '2', '3']:
    if input_str == '1':
      tool.add_user()
    elif input_str == '2':
      tool.show_all()
    elif input_str == '3':
      tool.search()
  elif input_str == '0':
    print('欢迎下次光临！')
    break
    pass
  else:
    print('您输入有误，请重新输入')