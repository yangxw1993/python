from pymysql import connect


class STUDENT(object):

    def __init__(self):
        # 创建数据库连接
        self.conn = connect(host="localhost", port=3306, user="root", password="", database="python_db", charset="utf8")

        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def run_sql(self, sql):
        self.cursor.execute(sql)
        for item in self.cursor.fetchall():
            print(item)

    def show_all_student(self):
        sql = 'SELECT * FROM student;'
        self.run_sql(sql)

    def show_man(self):
        sql = "SELECT * FROM student where age > 30;"
        self.run_sql(sql)

    def show_max_age(self):
        sql = "SELECT * FROM student where age = (select max(age) from student) ;"
        self.run_sql(sql)

    @staticmethod
    def show_menu(self):
        print('------查询用户信息--------')
        print('1: 所有用户')
        print('2. 所有的男性')
        print('3: 年龄最大的')
        print('4: 查询用户信息')
        return input('请输入功能对应得序号：')

    def query_info_by_id(self):
        student_id = input('请输入学生ID：')
        # 不安全
        # sql = f'SELECT * FROM student where id = {student_id};'
        # self.run_sql(sql)
        # 以下方式可以简单防止sql注入
        params = [student_id]
        self.cursor.execute('SELECT * FROM student where id=%s', params)
        for item in self.cursor.fetchall():
            print(item)

    def run(self):
        while True:
            num = self.show_menu(self)
            if num == '1':
                self.show_all_student()
            elif num == '2':
                self.show_man()
            elif num == '3':
                self.show_max_age()
            elif num == '4':
                self.query_info_by_id()
            else:
                print('输入有误，请重新输入')


def main():
    student = STUDENT()
    student.run()


if __name__ == '__main__':
    main()
