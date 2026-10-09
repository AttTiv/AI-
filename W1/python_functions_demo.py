# -*- coding: utf-8 -*-
"""
Python 函数定义用法入门示例 —— 面向有 C 语言基础的读者
======================================================
每个小节都标注了与 C 语言的对应/差异点。
运行方式：python3 python_functions_demo.py
"""


# ============ 1. 定义与调用：def + 冒号 + 缩进 ============
# C 语言：int add(int a, int b) { return a + b; }
# Python：不需要声明返回类型，也不需要大括号
def add(a, b):
    """两数相加（docstring 文档字符串，可用 help(add) 查看）"""
    return a + b


# ============ 2. 参数不需要声明类型 ============
# C 语言：int 参数就只能传 int
# Python：动态类型，传什么类型都行（甚至不同类型）
def describe(x):
    return f"值是 {x}，类型是 {type(x).__name__}"


# ============ 4. 返回多个值 ============
# C 语言：return 只能返回一个值；多个值要靠指针参数或结构体
# Python：return a, b 返回一个元组，自动拆包
def min_max(lst):
    return min(lst), max(lst)     # 返回 (最小值, 最大值)


# ============ 5. 默认参数 ============
# C 语言：没有默认参数（C++ 才有）
# Python：调用时可以省略有默认值的参数
def greet(name, greeting="你好"):
    return f"{greeting}，{name}"


# ============ 8. *args 可变参数 ============
# C 语言：... + va_list（va_start/va_arg/va_end，繁琐）
# Python：*args 把多余位置参数收进元组
def total(*args):
    return sum(args)


# ============ 9. **kwargs 关键字参数收集 ============
# C 语言：没有对应物
# Python：**kwargs 把多余关键字参数收进字典
def show_info(name, **kwargs):
    print(f"9) 姓名: {name}")
    for k, v in kwargs.items():
        print(f"   附加信息: {k} = {v}")


# ============ 12. 嵌套函数与闭包 ============
# C 语言：函数不能嵌套定义（GNU 扩展除外），没有闭包
# Python：函数里可以定义函数，并"记住"外层变量
def make_multiplier(factor):
    def multiply(x):
        return x * factor        # 闭包：记住 factor
    return multiply


# ============ 13. global 修改全局变量 ============
counter = 0

def increment():
    global counter              # 声明：修改的是全局变量
    counter += 1


def main():
    # ============ 1. 调用 ============
    print("1) add(3, 4) =", add(3, 4))

    # ============ 2. 动态类型参数 ============
    print("2) describe(42) =", describe(42))
    print("   describe('hi') =", describe("hi"))

    # ============ 3. 没有 return 返回 None ============
    # C 语言：void 函数没有返回值
    # Python：没写 return 的函数返回 None（类似 void，但 None 是个值）
    def do_nothing():
        pass                     # pass 占位，什么都不做

    r = do_nothing()
    print("3) 无 return 的函数返回:", r, "(None)")

    # ============ 4. 返回多个值（元组拆包） ============
    low, high = min_max([5, 2, 9, 1])
    print("4) min_max 返回两个值:", low, high)

    # ============ 5. 默认参数 ============
    print("5) greet('小明') =", greet("小明"))
    print("   greet('小明', '早上好') =", greet("小明", "早上好"))

    # ============ 6. 默认参数是可变对象的坑（经典） ============
    # C 语言：没有默认参数，没这个坑
    # Python：默认参数只在定义时求值一次，可变对象会被"共享"
    def append_item(item, lst=[]):     # 不推荐！默认参数用了可变对象
        lst.append(item)
        return lst

    print("6) 默认参数坑:")
    print("   第一次:", append_item(1))
    print("   第二次:", append_item(2), "(注意：还是同一个列表！)")
    # 正确做法：默认参数用 None，函数内新建
    def append_ok(item, lst=None):
        if lst is None:
            lst = []
        lst.append(item)
        return lst

    print("   正确写法 lst=None:", append_ok(1), append_ok(2))

    # ============ 7. 关键字参数 ============
    # C 语言：只能按位置传参
    # Python：可以用 参数名=值 传参，顺序随意
    def make_sentence(subject, verb, obj):
        return f"{subject}{verb}{obj}"

    print("7) 位置传参:", make_sentence("我", "吃", "苹果"))
    print("   关键字传参:", make_sentence(obj="苹果", subject="我", verb="吃"))

    # ============ 8. *args ============
    print("8) total(1,2,3,4) =", total(1, 2, 3, 4))

    # ============ 9. **kwargs ============
    show_info("小明", age=18, city="成都")

    # ============ 10. lambda 匿名函数 ============
    # C 语言：没有 lambda；要用函数指针 + 具名函数
    # Python：lambda 参数: 表达式 一行定义小函数
    square = lambda x: x * x
    print("10) lambda square(5) =", square(5))

    # ============ 11. 函数是一等公民 ============
    # C 语言：函数指针 int (*fp)(int)，语法繁琐
    # Python：函数可以直接传给别的函数
    words = ["banana", "apple", "cherry"]
    words.sort(key=len)            # key 参数接收一个函数
    print("11) sorted by len:", words)
    words.sort(key=lambda w: w[-1])  # 按最后一个字母排序
    print("    sorted by last char:", words)

    # ============ 12. 闭包 ============
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print("12) 闭包: double(5) =", double(5), " triple(5) =", triple(5))

    # ============ 13. global ============
    increment()
    increment()
    print("13) 调用两次 increment 后 counter =", counter)

    # ============ 14. 递归 ============
    # C 语言：同样支持递归
    # Python：有递归深度限制（默认 1000）
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    print("14) factorial(5) =", factorial(5))


if __name__ == "__main__":
    main()
#（注：内容由AI生成）
