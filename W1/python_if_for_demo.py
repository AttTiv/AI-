# -*- coding: utf-8 -*-
"""
Python 控制流：if 与 for 用法入门示例 —— 面向有 C 语言基础的读者
==============================================================
每个小节都标注了与 C 语言的对应/差异点。
运行方式：python3 python_if_for_demo.py
"""


def main():
    print("========== 一、if 判断 ==========")

    # ============ 1. 基本结构：if / elif / else ============
    # C 语言：if (x > 0) { } else if (x == 0) { } else { }
    # Python：if 条件:  elif 条件:  else:  —— 注意冒号和缩进
    score = 85
    if score >= 90:
        grade = "优秀"
    elif score >= 60:      # 对应 C 的 else if
        grade = "及格"
    else:
        grade = "不及格"
    print("1) score =", score, "→", grade)

    # ============ 2. 缩进就是"大括号" ============
    # C 语言：用 { } 圈定代码块
    # Python：用缩进(通常 4 空格)圈定代码块，缩进错了程序都跑不了
    x = 5
    if x > 0:
        print("2) x 是正数")          # 缩进 → 属于 if
    print("   这行不缩进 → 无条件执行")

    # ============ 3. 真值判断：0/空/None 都是假 ============
    # C 语言：0 为假，非 0 为真（数字直接判断）
    # Python：除 0 外，空字符串/空列表/空字典/None 也都是假
    if 0:        print("3) 0 是真的")          # 不会打印
    if "" :      print("   空串是真的")        # 不会打印
    if []:       print("   空列表是真的")      # 不会打印
    if None:     print("   None 是真的")       # 不会打印
    if "hi":     print("3) 非空字符串是真的 ✓")

    # ============ 4. 逻辑运算：and / or / not ============
    # C 语言：&& / || / !
    # Python：and / or / not；且短路求值
    a, b = 3, 5
    if a > 0 and b > 0:
        print("4) and 两个都成立 → True")
    if a > 0 or b < 0:
        print("   or 一个成立 → True")
    if not a > 10:
        print("   not 取反 → True")

    # Python 的 and/or 返回操作数本身（C 的 &&/|| 只返回 0/1）
    result = 0 or "默认值"      # 返回右边的"默认值"
    print("   or 短路返回:", result)
    result2 = "有值" and "也返回这个"
    print("   and 短路返回:", result2)

    # ============ 5. 链式比较 ============
    # C 语言：x > 0 && x < 10 要写两个条件
    # Python：0 < x < 10 直接连写
    x = 5
    if 0 < x < 10:
        print("5) 链式比较 0 < x < 10 成立 ✓ (C 里要写 x>0 && x<10)")

    # ============ 6. 三元表达式 ============
    # C 语言：条件 ? a : b
    # Python：a if 条件 else b（注意顺序不同！）
    age = 20
    label = "成年" if age >= 18 else "未成年"   # 先写成立的值
    print("6) 三元表达式:", label, "(C 写: age>=18 ? 成年 : 未成年)")

    # ============ 7. if 块不产生新作用域 ============
    # C 语言：if (x > 0) { int y = 1; }  y 在块外不可见
    # Python：if 内定义的变量，块外照常用（回顾变量篇第 8 节）
    if x > 0:
        y = 100
    print("7) if 块内定义的 y 块外可见:", y)

    # ============ 8. is 与 == 的区别 ============
    # C 语言：== 比值；指针 == 比地址
    # Python：== 比内容；is 比身份(是不是同一个对象，类似比地址)
    s1 = "abc"
    s2 = "abc"
    print("8) s1 == s2:", s1 == s2, " s1 is s2:", s1 is s2,
          "(小字符串可能缓存，is 结果不一定)")
    lst_a = [1, 2]
    lst_b = [1, 2]
    print("   列表: lst_a == lst_b:", lst_a == lst_b,
          " lst_a is lst_b:", lst_a is lst_b, "(内容相同但对象不同)")

    print()
    print("========== 二、for 循环 ==========")

    # ============ 9. 本质：for...in 是"遍历"，不是计数器 ============
    # C 语言：for (i = 0; i < n; i++) 三部分：初始化/条件/步进
    # Python：for x in 序列: 逐个取出元素（foreach 风格）
    fruits = ["苹果", "香蕉", "樱桃"]
    for f in fruits:
        print("9) 遍历元素:", f)

    # ============ 10. range()：Python 的"计数器" ============
    # C 语言：for (i = 0; i < 5; i++)  ← 左闭右开 [0,5)
    # Python：for i in range(5)      ← 生成 0,1,2,3,4（不包含 5）
    print("10) range(5):", end=" ")
    for i in range(5):
        print(i, end=" ")
    print()
    # range(起点, 终点, 步长) 对应 C 的 i=start; i<end; i+=step
    print("    range(1, 6):", list(range(1, 6)))        # [1,2,3,4,5]
    print("    range(0, 10, 2):", list(range(0, 10, 2)))  # [0,2,4,6,8]

    # ============ 11. 遍历各种序列 ============
    # C 语言：字符串/数组都要用下标循环
    # Python：字符串、列表、字典都能直接 for...in
    for ch in "abc":
        print("11) 遍历字符串字符:", ch)
    d = {"name": "小明", "age": 18}
    for k in d:
        print("    遍历字典 key:", k)
    for k, v in d.items():
        print("    遍历键值对:", k, "=", v)

    # ============ 12. enumerate()：下标+值一起拿 ============
    # C 语言：for 循环里用 i 当下标
    # Python：enumerate(lst) 同时给下标和元素
    colors = ["red", "green", "blue"]
    for i, color in enumerate(colors):
        print("12) 下标", i, ":", color)

    # ============ 13. break / continue ============
    # C 语言：完全相同
    # break：立即跳出整个循环；continue：跳过本轮，进入下一轮
    for i in range(10):
        if i == 3:
            continue      # 跳过 3，继续 4...
        if i == 6:
            break         # 到 6 就彻底停
        print("13) i =", i)
    print("    (跳过了 3，在 6 处 break)")

    # ============ 14. for...else：Python 独有 ============
    # C 语言：没有这个语法
    # 循环正常跑完(没被 break 打断)才执行 else；break 了就跳过 else
    for i in range(5):
        if i == 99:        # 永不成立
            break
    else:
        print("14) for...else: 循环正常结束，执行 else ✓")

    for i in range(5):
        if i == 2:         # 成立 → break
            break
    else:
        print("    这行不会打印")
    print("    (第二次循环在 2 处 break，else 没执行)")

    # ============ 15. while 循环 ============
    # C 语言：while (条件) { } 基本一样
    # Python：while 条件: 注意冒号和缩进
    n = 0
    while n < 3:
        print("15) while 循环 n =", n)
        n += 1

    # ============ 16. 遍历时修改列表的坑 ============
    # C 语言：循环内删元素，索引会错位
    # Python：遍历列表时删除元素会"跳过"相邻元素！
    nums = [1, 2, 3, 4, 5]
    for x in nums:          # 错误示范：遍历原列表
        nums.remove(x)      # 想清空列表
    print("16) 边遍历边删(错误):", nums,
          "(删 1 后 2 前移被跳过，只删了一半)")

    nums2 = [1, 2, 3, 4, 5]
    for x in nums2[:]:      # 正确：遍历副本 nums2[:]
        nums2.remove(x)
    print("    遍历副本删(正确):", nums2, "(全部删干净)")


if __name__ == "__main__":
    main()
#（注：内容由AI生成）
