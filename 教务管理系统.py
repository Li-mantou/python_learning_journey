class Student:
    def __init__ (self,name,chinese,math,english):
        self.name=name
        self.chinese = chinese
        self.math = math
        self.english = english
        print("学生信息录入成功")



    def __str__(self):
        return f"学生为{self.name},语文成绩为{self.chinese},数学成绩为{self.math},英语成绩为{self.english},总分为{self.chinese + self.math + self.english}"

    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english
        print("修改完毕")


class Education_system:
    system_version = "1.0"
    system_name = "教务系统"

    def __init__(self):
        self.student_list = []
# 添加学生的成绩
    def add_student(self):
        name = input("请输入学生姓名")
        for s in self.student_list:
            if s.name == name:
                print("此学生信息存在")
                return
        chinese = int(input("输入学生的语文成绩"))
        math = int(input("输入学生的数学成绩"))
        english = int(input("输入学生的英语成绩"))
# 验证成绩的范围
        if 0 <= chinese <=100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
        else:
            print("各科成绩要正常合法!!!")
# 修改学生成绩
    def update_student(self):
        name = input("输入您所要修改的学生名字:")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩:{s}")
                chinese = int(input("输入学生修改后的语文成绩"))
                math = int(input("输入学生的修改后数学成绩"))
                english = int(input("输入学生修改后的英语成绩"))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print(f"当前成绩:{s}")
                    return

                else:
                    print("各科成绩要正常合法!!!")
                    print("修改失败")
                    return
        else:
            print("未查询到该学生,请输入学生正确信息")
            return

# 删除学生成绩
    def delete_student(self):
        name = input("输入您要删除的信息的学生名字:")
        for s in self.student_list:
            if s.name == name:
                print(f"当前学生信息为{s},删除成功")
                self.student_list.remove(s)
                return
        else:
            print("未能找到此信息,操作不合法")
            return


# 查询学生成绩
    def find_student(self):
        name = input("输入您要查询的学生姓名")
        for s in self.student_list:
            if s.name == name:
                return print(f"此学生的信息为:{s}")
        else:
            print("未能成功查询")
            return
# 罗列学生信息
    def print_student(self):
        for s in self.student_list:
            if s is None:
                print("此名单没有信息")
            else:
                print(s)
# 添加运行代码
    def run(self):
        print(f"欢迎使用{Education_system}")
        while True:
            print()
            print()
            print("1,添加学生")
            print("2,修改学生")
            print("3,删除学生")
            print("4,查询学生")
            print("5,罗列名单")
            print("6.安全退出")
            c = input("输入您的操作")
            if c == "1":
                self.add_student()
            elif c == "2":
                self.update_student()
            elif c == "3":
                self.delete_student()
            elif c == "4":
                self.find_student()
            elif c == "5":
                self.print_student()
            elif c == "6":
                print("正在安全退出")
                break
            else:
                print("非法操作")
                continue



if __name__ == "__main__":
    education_system = Education_system()
    education_system.run()