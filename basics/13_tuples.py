# # 1.现有两个变量，分别为:a = 10，b =20，现需要将这两个变量值交换，然后输出到控制台。
# a =10
# b=20
# b,a = a,b
# print(f"{a} {b}")
#
# # 现有三个变量，分别为:a = 100,b =200,c = 300，现需要将这三个变量值进行交换，将
# # a,b，c的值分别赋值给c,a,b，并将其输出到控制台。
# a = 100
# b = 200
# c = 300
# c,a,b =a,b,c
# print(f"{a} {b} {c}")
# 根据提供的学生成绩单，完成如下需求:
# 1.计算每个学生的总分、各科平均分，然后一并输出出来。
students = (
("S001", "王林", 85, 92,78),
("S002","李慕婉",92,88,95),
("S003", "十三",78, 85,82),
("S004", "曾牛",88,79,91),
("S005","周轶",95,96,89),
("S006","王卓",76,82,77),
("S007","红蝶",89,91,94),
("S008","徐立国",75,69,82),
("S009","许木",86,89,98),
("S010","遁天",66,59,72)
)
# 方式一
print("学号\t\t姓名\t\t语文\t\t数学\t\t姓名\t\t总分\t\t平均分\t\t")
# for i in students:
#     total = i[2]+i[3]+i[4]
#     avg = total/3
#     print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]} \t {i[4]} \t {total} \t {avg:.1f}")

# 方式二
for id,name,Chinese,Math,English in students:
    total =  Chinese+Math+English
    avg = total/3
    print(f"{id} \t {name} \t {Chinese} \t {Math} \t {English} \t {total} \t {avg:.1f}")

# 2.统计各科成绩的最低分、最高分、平均分，并输出。
chinese = [i[2] for i in students]
math= [i[3] for i in students]
english = [i[4] for i in students]

print(f"语文:最小值{min(chinese)},最大值:{max(chinese)},平均值:{sum(chinese)/len(chinese)}")
print(f"数学:最小值{min(math)},最大值:{max(math)},平均值:{sum(math)/len(math)}")
print(f"英语:最小值{min(english)},最大值:{max(english)},平均值:{sum(english)/len(english)}")

# 3.查找成绩优秀(平均分大于90)的学生，并输出。
print("优秀学生名单如下(平均分>90)")
# for i in students:
#     total = i[2]+i[3]+i[4]
#     avg = total/3
#     if avg >90:
#         print(f"学号:{i[0]} 姓名:{i[1]} 平均分:{avg:.1f}")

for id,name,Chinese,Math,English in students:
    total = Chinese+Math+English
    avg = total/3
    if avg >90:
        print(f"学号:{id} 姓名:{name} 平均分:{avg:.1f}")














