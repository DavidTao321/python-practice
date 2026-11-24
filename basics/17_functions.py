# 函数的参数与返回值
#函数1:计算圆的面积
# def circle(r):
#     area = 3.14*r*r
#     return area
#
# r_circle = circle(10)
# print(r_circle)

#函数2:计算长方形的面积
# def rectangle(l,w):
#     """
#     :param l:  长方形的长
#     :param w: 长方形的宽
#     :return: area 长方形的面积
#
#     """
#     area = l * w
#     return area
#
# print(rectangle(1,2))
# help(rectangle)

# 1.定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积= 底 *高/2)。
# def avc(l,w):
#     """
#     传入的底和高计算三角形面积的函数
#     :param l: 三角形的底部
#     :param w: 三角形的高
#     :return: area 三角形的面积
#     """
#     area = l * w /2
#     return  area
#
# print(avc(5,6))
#
#.定义一个函数:计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)。
#
# def count(i):
#     """
#
#     :param i:输入的字符串
#     :return: 元音的个数
#     """
#     num = 0
#     for s in i :
#         if s in "aeiouAEIOU":
#             num += 1
#     return num
#
# print(count("ds"))
#3.定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)
# def score(i):
#     return round(max(i),1),round(min(i),1),round(sum(i)/len(i),1)
#
# list1 = [589, 609, 605, 643, 677, 455, 477, 489, 503]
# big,small,sum1 = score(list1)
# print(big)
# print(small)
# print(sum1)
#
#
#
#















