# # 遍历
# dict1={"张三":323,"李四":323}
# for k in dict1.keys():
#     print(f"{k}:{dict1[k]}")
#
# for item in dict1.items():
#     print(f"{item[0]:{item[1]}}")
#
# for k,v in dict1.items():
#     print(f"{k}:{v}")

# 案例:
# 购物车系统###添加购物车修改购物车删除购物车查询购物车5.退出购物车
# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
# 具体功能如下:
# 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车:将购物车中的商品信息展示出来，格式为:“商品名称:xxx，商品价格:xxx，商品数量:xxx”。
# 5.退出购物车
# 结构: shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标":{...}}
#
# print("#############购物车系统#############")
# print("#           1.添加购物车           #")
# print("#           2.修改购物车           #")
# print("#           3.删除购物车           #")
# print("#           4.查询购物车           #")
# print("#           5.退出购物车           #")
# print("##################################")
# dict1 = {}
# while True:
#    i = input("请选择要执行的操作(1-5):")
#    match i:
#       case "1":
#          goods_name = input("请输入商品名称:")
#          goods_price = input("请输入商品价格:")
#          goods_num = input("请输入商品数量:")
#          if goods_name in dict1:
#             print("商品存在,请重新输入")
#          else:
#             dict1[goods_name] = {"price": goods_price, "num": goods_num}
#             print("商品添加完毕")
#       case "2":
#          goods_name = input("请输入要修改商品名称:")
#
#          if goods_name not in dict1:
#             print("商品不存在,请重新输入")
#             continue
#          goods_price = input("请输入要修改商品价格:")
#          goods_num = input("请输入要修改商品数量:")
#          dict1[goods_name] = {"price": goods_price, "num": goods_num}
#          print("商品修改完毕")
#       case "3":
#          goods_name = input("请输入要删除商品名称:")
#          if goods_name in dict1:
#             del dict1[goods_name]
#             print("商品删除完毕")
#          else:
#             print("该商品不存在")
#       case "4":
#          for name in dict1.keys():
#             info = dict1[name]
#             print(f"商品名称:{name},商品价格:{info['price']},商品数量:{info['num']}")
#       case "5":
#          print("bye")
#          break
#       case _:
#          print("非法输入!!")
#
#
#
