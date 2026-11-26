# 1.定义一个函数，根据传入的数字，计算该数字阶乘的结果。
# 递归函数
def fact(a):
     if a == 1:
         return 1
     else:
         return a * fact(a - 1)
b = input("请输入阶乘的数字:")
print(fact(int(b)))
