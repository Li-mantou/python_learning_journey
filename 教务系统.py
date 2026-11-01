# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：



# 2. 修改学生信息：
# 要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，
# 输入完成后修改学员信息。

# 3. 删除学生信息：
# 要求输入要删除的学生姓名，根据姓名删除学生信息。

# 4. 查询学生信息：
# 要求输入要查询的学生姓名，根据姓名查询学生信息并输出。

# 5. 列出所有学生：
# 遍历所有学生信息并输出。

# 6. 统计班级成绩：
# 统计班级语文、数学、英语成绩的最高分、最低分、平均分，
# 以及语文、数学、英语最高分和最低分的学员姓名。

# 7. 退出系统。
menu = """
#####     教务系统     #####
#      1. 添加学生         #
#      2. 修改学生         #
#      3. 删除学生         #
#      4. 查询学生         #
#      5. 列出学生         #
#      6. 统计成绩         #
#      7. 安全退出         #
"""

print(menu)
student = {}
while True:
    do = input("请输入你的操作:")

    if do == "1":# 1. 添加学生信息： 根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        name = input("录入学生姓名:")
        chinese = float(input("录入语文成绩:"))
        math = float(input("录入数学成绩"))
        english = float(input("录入英语成绩:"))
        if name in student:
            print("学生已存在")
        else:
            student[name] = {"语文":chinese,"数学":math,"英语":english}
            print("添加完毕")
    elif do == "2":
        name = input("录入学生姓名:")
        chinese = float(input("录入语文成绩:"))
        math = float(input("录入数学成绩"))
        english = float(input("录入英语成绩:"))
        if name not in student:
            print("学生不存在")
        else:
            student[name] = {"语文":chinese,"数学":math,"英语":english}
    elif do == "3": # 要求输入要删除的学生姓名，根据姓名删除学生信息。
        if name not in student:
            print("学生不存在")
        else:
            del student[name]
    elif do == "4":# 要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        name = input ("输入你要查询的学生姓名")
        if name not in student:
            finds = student[name]
            print("非法操作")
        else:
            print(f"您查询的学生姓名为{name},语文成绩为{finds['语文']},数学成绩为{finds['数学']},英语成绩为{finds['英语']}")
    elif do == "5":# 遍历所有学生信息并输出
        for name in student.keys():
            finds = student[name]
            print(f"{name}的语文成绩为{finds['语文']},数学成绩为{finds['数学']},英语成绩为{finds['英语']}")
    elif do == "6":# 统计班级语文、数学、英语成绩的最高分、最低分、平均分， 以及语文、数学、英语最高分和最低分的学员姓名。
        scores = [student[name]['语文'] for name in student]
        for name in student:
            if student[name]['语文'] == max(scores):
                print(f"语文的最高分为{scores},姓名为{name}]")
        for name in student:
            if student[name]['语文'] == min(scores):
                print(f"语文的最低分为{scores},姓名为{name}]")
        print(f"语文平均分{sum(scores)/len(scores)}")

        scores = [student[name]['数学'] for name in student]
        for name in student:
            if student[name]['数学'] == max(scores):
                print(f"数学的最高分为{scores},姓名为{name}]")
        for name in student:
            if student[name]['数学'] == min(scores):
                print(f"数学的最低分为{scores},姓名为{name}]")
        print(f"数学平均分{sum(scores) / len(scores)}")

        scores = [student[name]['英语'] for name in student]
        for name in student:
            if student[name]['英语'] == max(scores):
                print(f"英语的最高分为{scores},姓名为{name}]")
        for name in student:
            if student[name]['英语'] == min(scores):
                print(f"英语的最低分为{scores},姓名为{name}]")
        print(f"英语平均分{sum(scores)/len(scores)}")

    elif do == "7":
        print("正在退出")
        break
    else:
        print("无效操作")