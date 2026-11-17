# 循环嵌套:根据输入的长方形的长度m，宽度n
# length =int(input("请输入长方形的长度:"))
# width  = int(input("请输入长方形的宽度:"))
# for j in range(length):
#     for i in  range(width):
#         print("*", end="  ")
#     print()


#打印99乘法表
# for i in range(1,10):
#     for j in  range(1,i+1):
#            print(f"{j}*{i}={j*i}",end=" ")
#     print()
#

# 需求1:根据输入的直角边的边长，打印等腰直角三角形(如下为直角边为5的等腰直角三角形)
# a = int(input("请输入等腰直角的边长:"))
#
# for j in range(a):
#     for i in range(j+1):
#         print("*",end=" ")
#     print()
#
#
#
# 需求2:根据输入的数字，打印对应的数字金字塔
# a = int (input("请输入一个数字:"))
# for j in range(1,a):
#     for i in range(1,j+1):
#         print(f"{i}",end=" ")
#     print()
#需求3:打印国际象棋棋盘
# for j in range(1,9):
#     for i in range(1,9):
#         if (i+j)%2==0:
#             print("x",end=" ")
#         else:
#             print("√",end=" ")
#     print()
#
#
