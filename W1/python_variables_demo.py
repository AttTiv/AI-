# -*- coding: utf-8 -*-
"""
Python 变量用法入门示例 —— 面向有 C 语言基础的读者
=====================================================
每个小节都标注了与 C 语言的对应/差异点。
运行方式：python3 python_variables_demo.py
（程序中有 input()，会等待你输入名字）
"""


# 模块级全局变量（第 9 节演示用）
counter = 0


def main():
    # ============ 1. 声明与赋值：无需声明类型 ============
    # C 语言：   int x;      /* 必须先声明类型 */
    #            x = 10;
    # Python：直接赋值即创建变量，类型由值自动推断
    x = 10
    print("1) 直接赋值: x =", x, " 类型:", type(x).__name__)

    # ============ 2. 动态类型：变量可改绑不同类型 ============
    # C 语言：x 一旦声明为 int，就不能再存字符串
    # Python：变量只是"名字"，可随时绑定到不同类型的对象
    x = "hello"          # 合法！x 现在是字符串
    print("2) 重新绑定为字符串: x =", x, " 类型:", type(x).__name__)

    # ============ 3. 整数任意精度，没有溢出 ============
    # C 语言：int 通常 4 字节，10**30 会溢出
    # Python：int 无大小限制
    big = 10 ** 30
    print("3) 大整数(无溢出):", big)

    # ============ 4. 多重赋值与交换 ============
    a, b = 1, 2
    print("4) 多重赋值: a =", a, " b =", b)
    a, b = b, a          # C 里交换需要临时变量 tmp
    print("   一行交换后: a =", a, " b =", b)

    # ============ 5. "常量"：约定而非强制 ============
    # C 语言：const int MAX = 100; 编译器强制不可改
    # Python：没有真正的常量，全大写只是命名约定
    MAX = 100
    MAX = 200            # 不会报错！（只是不推荐）
    print("5) 全大写是常量约定，但可被修改:", MAX)

    # ============ 6. 输入输出：无需格式说明符 ============
    # C 语言：scanf("%d", &n);   printf("%d", n);
    # Python：input() 返回字符串，print() 自动格式化
    name = input("6) 请输入你的名字: ")
    print("   你好,", name)

    # ============ 7. 类型转换 ============
    # C 语言：atoi() / atof() / sprintf()
    num = int("42")      # 字符串 -> 整数（对应 atoi）
    f = float("3.14")    # 字符串 -> 浮点数
    s = str(100)         # 整数 -> 字符串
    print("7) 转换: int('42') =", num, " float('3.14') =", f, " str(100) =", s)

    # ============ 8. 没有块级作用域！ ============
    # C 语言：if (1) { int y = 5; }  y 在块外不可见
    # Python：if/for/while 不产生新作用域
    if True:
        y = 5
    print("8) if 块内定义的 y 在块外可见:", y)   # C 中这行会编译报错

    # ============ 9. 局部变量与 global ============
    # 函数内赋值默认创建局部变量；修改模块级全局变量需 global 声明
    def add_one():
        global counter   # 声明：我要修改的是模块级全局变量
        counter += 1

    add_one()
    print("9) 用 global 修改全局变量后 counter =", counter)

    # ============ 10. 变量是"引用"，不是装值的盒子 ============
    # C 语言：int p = 1; int q = p;  复制的是值
    # Python：p 和 q 是名字，绑定到同一个对象；id() 类似 &p 看地址
    p = 1
    q = p
    print("10) q = p 后, p 与 q 的 id 相同:", id(p), id(q),
          "(小整数有缓存，指向同一对象)")

    lst1 = [1, 2, 3]
    lst2 = lst1          # 复制的是"引用"，不是数据！
    lst2.append(4)
    print("    列表是可变对象, 修改 lst2 后 lst1 =", lst1, "(两者指向同一列表)")

    # 想真正复制列表，用切片
    lst3 = lst1[:]
    lst3.append(5)
    print("    切片复制后 lst1 =", lst1, " lst3 =", lst3)

    # ============ 11. 命名规范 ============
    # C 语言：int studentCount; 驼峰或下划线均可
    # Python：官方推荐 PEP 8 —— 变量用 snake_case（全小写+下划线）
    student_count = 3
    print("11) 推荐命名 snake_case: student_count =", student_count)

    # ============ 12. 没有指针，但可变对象天然"引用传递" ============
    # C 语言：void inc(int *p) { (*p)++; }   要传地址
    # Python：可变对象(列表/字典等)直接传引用
    def inc(lst):
        lst.append(100)

    nums = [1]
    inc(nums)
    print("12) 函数内修改列表(相当于传指针效果): nums =", nums)


if __name__ == "__main__":
    main()
#（注：内容由AI生成）
