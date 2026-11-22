# 遍历
dict1={"张三":323,"李四":323}
for k in dict1.keys():
    print(f"{k}:{dict1[k]}")
    
for item in dict1.items():
    print(f"{item[0]:{item[1]}}")

for k,v in dict1.items():
    print(f"{k}:{v}")