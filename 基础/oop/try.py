try:
  input_str = int(input('请输入数字：'))
  result = input_str/8
  print(result)
except Exception as result:
  print(f'未知错误{result}')