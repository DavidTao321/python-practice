# python-practice

Python 练习仓库 —— 记录每天的学习代码。

## 目录约定

随着练习增加，计划按下面的方式组织：

```
python-practice/
├── README.md
├── .gitignore
├── basics/        # 基础语法、数据类型、流程控制
├── oop/           # 类与对象
├── stdlib/        # 标准库练习（文件、json、datetime 等）
├── exercises/     # 零散练习题
└── tests/         # 给练习代码配的测试
```

## 已上传练习（按上传时间排序）

| 序号 | 文件 | 上传时间 | 内容 |
| --- | --- | --- | --- |
| 01 | [basics/01_project_1.py](basics/01_project_1.py) | 2026-11-11 | 平均数、梯形面积、圆周长与面积、BMI |
| 02 | [basics/02_if_statements.py](basics/02_if_statements.py) | 2026-11-12 | if 条件判断（B 站登录模拟） |
| 03 | [basics/03_leap_year.py](basics/03_leap_year.py) | 2026-11-15 | 闰年、奇偶、成年、正负、及格判定 |
| 04 | [basics/04_if_advanced.py](basics/04_if_advanced.py) | 2026-11-16 | elif 多分支、match 模式匹配（登录、成绩、折扣、三角形、计算器、游戏指令） |
| 05 | [basics/05_loops_and_range.py](basics/05_loops_and_range.py) | 2026-11-17 | while / for / range()：求和、遍历字符串、else 子句 |
| 06 | [basics/06_nested_loops.py](basics/06_nested_loops.py) | 2026-11-17 | 嵌套循环：长方形、99 乘法表、直角三角形、数字金字塔、国际象棋棋盘 |
| 07 | [basics/07_flow_control_practice.py](basics/07_flow_control_practice.py) | 2026-11-18 | 流程控制练习：登录重试循环、猜数字、1-1000 内 5 的倍数求和、统计字符串中 a 与 k 的个数（代码以注释形式保留） |
| 08 | [basics/08_lists.py](basics/08_lists.py) | 2026-11-19 | 列表练习：列表遍历、十个数排序取最值、合并两个列表并去重、1-20 平方列表、偶数平方（代码以注释形式保留） |
| 12 | [basics/12_strings.py](basics/12_strings.py) | 2026-11-20 | 字符串练习：邮箱格式验证、回文判断、10 个字符串反转后转大写并遍历输出 |
| 13 | [basics/13_tuples.py](basics/13_tuples.py) | 2026-11-20 | 元组练习：变量值交换、学生成绩单统计（总分/平均分/各科最值与均值/优秀学生筛选） |
| 14 | [basics/14_sets.py](basics/14_sets.py) | 2026-11-21 | 集合练习：交集/差集/并集，统计每个学生选修课程数量（课堂练习，示例代码以注释形式保留） |
| 15 | [basics/15_dicts.py](basics/15_dicts.py) | 2026-11-22 | 字典遍历：keys() / items() / for k, v in d.items() 三种写法 |

> 新练习按上传顺序依次加 `01_`、`02_`… 数字前缀，仅用于排序，文件名保持可读。

## 环境

需要 Python 3.8 或更高版本（本机已有 3.13 / 3.14）。

```bash
# 建议每个练习目录单独建虚拟环境
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# 运行单个练习文件
python basics/01_project_1.py
```

## 说明

- 仓库从空的 README 起步，代码会随练习逐步加入。
- `__pycache__/`、`.venv/`、IDE 配置等已在 `.gitignore` 中排除，不会误提交。
