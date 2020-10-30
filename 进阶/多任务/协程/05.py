"""" 复制到ipython3 中运行"""

import urllib.request

req = urllib.request.urlopen('http://www.sina.com.cn')
req.read()
