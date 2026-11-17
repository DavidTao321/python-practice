# numbers = int(input("请输入一个数字:"))
# if numbers>0:
#     print(f"{numbers}是正数")
# elif numbers<0:
#     print(f"{numbers}是负数")
# else:
#     print(f"{numbers}是0")
from numpy.f2py.crackfortran import usermodules

# 根据输入用户名、密码进行登录系统。
# 用户名、密码为 admin/666888 或root/547527或zhangsan/123456,则输出登录成功
# 否则就提示用户名或密码错误

# user1 = "admin"
# user2 = "root"
# user3 = "zhangsan"
# password1 = "666888"
# password2 = "547527"
# password3 = "123456"
# user = input("请输入用户名:")
# password = input("请输入用户密码:")
# if user==user1 and password==password1:
#     print("登录成功")
# elif user==user2 and password==password2:
#     print("登录成功")
# elif user==user3 and password==password3:
#     print("登录成功")
# else:
#     print("登录失败")


#根据输入的考试成绩，判断成绩等级。
# 大于等于85分为优秀
# 60-85分为及格
# 否则就是不及格
# score = int(input("请输入考试成绩:"))
# if score>85:
#     print("优秀")
# elif 60<score<85:
#     print("良")
# else:
#     print("不及格")
#购物折扣计算:根据输入的购物车的商品总额，以及如下的折扣规则，计算实际应付的金额。
# 金额>=500:8折
# 300<=金额<500:9折
# 100<= 金额<300:95折
# 金额<100:无折扣
#
# money =float(input("请输入金额:"))
# if money >=500:
#     money *=0.8
#     print(f"折扣后的金额为{money}")
# elif 300<=money<500:
#     money *=0.9
#     print(f"折扣后的金额为{money}")
# elif 100<=money<300:
#     money *=0.95
#     print(f"折扣后的金额为{money}")
# else :
#     print(f"折扣后的金额为{money}")

# 三角形类型判断:根据输入的三个边的边长(正整数)，判定是等边三角形、等腰三角形、普通三角
# 形，还是不能构成三角形。
# 构成三角形的条件:两边之和大于第三边
# 三角形判定规则:
# 三个边都相等:等边三角形
# 两个边相等:等腰三角形
# 三个边都不相等:普通三角形

# length1 =float(input("请输入三角形边长:"))
# length2 =float(input("请输入三角形边长:"))
# length3 =float(input("请输入三角形边长:"))
# if length1+length2>length3 and length1+length3>length2 and length3+length2>length1:
#     if length1 == length2 == length3:
#         print("该三角形为等边三角形")
#     elif length1 == length2 or length1 == length3 or length2 == length3:
#         print("该三角形为等腰三角形")
#     else:
#         print("是普通三角形")
# else:
#     print("无法构成三角形")
#
# 实现一个计算器，可以实现+-*/运算，用户输入需要运算的两个数以及运算符之后，就可以进行计算。
# num1 =float(input("请输入一个数字:"))
# num2 =float(input("请输入一个数字:"))
# operation = input("请输入运算符:")
# match operation:
#     case "+":
#         print(f"num1+num2={num1+num2}")
#     case "-":
#         print(f"num1-num2={num1 - num2}")
#     case "*":
#         print(f"num1*num2={num1 * num2}")
#     case "/" if num2!= 0:
#         print(f"num1/num2={num1/num2}")
#     case _:
#         print("输入有误")
#
#
# user = input("请输入玩家指令:")
# match user:
#     case "上" | "w" | "W":
#         print("角色向上移动")
#     case "下" | "s" | "S":
#         print("角色向下移动")
#     case "左" | "a" | "A":
#         print("角色向左移动")
#     case "右" | "d" | "D":
#         print("角色向右移动")
#     case "跳" | " ":
#         print("角色向右移动")
#     case "攻击" | "j" | "J":
#         print("角色攻击")
#     case "退出" | "esc" | "ESC":
#         print("角色退出")
#     case _:
#         print("无效操作")









