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

## 环境

需要 Python 3.8 或更高版本（本机已有 3.13 / 3.14）。

```bash
# 建议每个练习目录单独建虚拟环境
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# 运行单个练习文件
python exercises/hello.py
```

## 说明

- 仓库从空的 README 起步，代码会随练习逐步加入。
- `__pycache__/`、`.venv/`、IDE 配置等已在 `.gitignore` 中排除，不会误提交。
