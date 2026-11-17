# 需求:结合前面学习的输入输出及if条件判断的知识，完成B站登录功能的实现(正确账号和密码为
# 18888888888/666888)
account = input("请输入账号:")
password = input("请输入密码:")
if account =="18888888888" and password =="666888":
    print("登录成功")
if account !="18888888888" or password !="666888":
    print("账号/密码错误")