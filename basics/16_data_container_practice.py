# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下:
# 1.添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2.修改学生信息:要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3.删除学生信息:要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4.查询学生信息:要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5.列出所有学生:遍历所有学生信息并输出。
# 6.统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分,以及语文、数学、英语最高分和最低分的学员姓名。
# 7.退出系统。

# top = [n for n, info in dict1.items() if float(info[key]) == max(values)]
# low = [n for n, info in dict1.items() if float(info[key]) == min(values)]
# top = []                                      # 1. 空列表，准备装名字
# for n, info in dict1.items():                 # 2. 遍历 键值对：(姓名, 成绩字典)
#     if float(info[key]) == max(values):       # 3. 这个人的该科分数 == 班级最高分？
#         top.append(n)                         # 4. 是 → 加入列表

print("""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 1.添加学生信息   2.修改学生信息    3.删除学生信息    4.查询学生信息      5.列出所有学生    6.统计班级成绩    7.退出系统  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n""")
dict1 = {}
while True:
    choice = input("请选择要执行的操作(1-7):")
    match choice:
        case "1":
            name = input("请输入学生姓名:")
            lang = input("请输入学生的语文成绩:")
            math = input("请输入学生的数学成绩:")
            English = input("请输入学生的英语成绩:")
            if name in dict1:
                print("输入的学生已存在列表内")
            else:
                dict1[name] = {'lang': lang, 'math': math, 'English': English}
                print("添加成功!!!")
        case "2":
            name = input("请输入要修改的学生姓名:")
            lang = input("请输入学生的语文成绩:")
            math = input("请输入学生的数学成绩:")
            English = input("请输入学生的英语成绩:")
            if name not in dict1:
                print("输入的学生不存在列表内")
            else:
                dict1[name] = {'lang': lang, 'math': math, 'English': English}
                print("修改成功!!!")
        case "3":
            name = input("请输入学生姓名:")
            if name in dict1:
                del dict1[name]
                print("删除成功!!!")
            else:
                print("为查询到该学生信息?")
        case "4":
            student = input("请输入姓名:")
            if student in dict1:
                for name in dict1:
                    info = dict1[name]
                    print(
                        f"学生姓名:{name},语文成绩为:{info['lang']},数学成绩为:{info['math']},英语成绩为:{info['English']}")
            else:
                print("未查询到学生姓名??")
        case "5":
            print(f"所有学生名单:{dict1.items()}")
        case "6":
            if not dict1:
                print("还没有任何学生信息，无法统计")
                continue

            print(f"【班级成绩统计】(共 {len(dict1)} 人)")
            for key,label in [("lang","语文"),("math","数学"),("English","英语")]:
                values = [float(info[key])for info in dict1.values()]
                average = sum(values)/len(values)
                top = [ n for n ,info in dict1.items() if float(info[key]) == max(values)]
                low = [ n for n,info in dict1.items() if float(info[key]) ==min(values)]
                print(f"{label}:最高{max(values)}"
                      f"最低{min(values)}"
                      f"平均:{average:.1f}")
        case "7":
            print("bye")
            break
        case _:
            print("输入错误!!!!")
