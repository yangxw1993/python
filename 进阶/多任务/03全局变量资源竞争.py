import time
import threading

class MyThread(threading.Thread):
  def run(self):
    self.login()
    print(f'this is {self.name}')
  def login(self):
    print('this is login')

def main():
  t = MyThread()
  t.start()


if __name__ == '__main__':
  main()