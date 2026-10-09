# -*- coding: utf-8 -*-
"""
Python 列表(list)与字典(dict)用法入门示例 —— 面向有 C 语言基础的读者
==============================================================
每个小节都标注了与 C 语言的对应/差异点。
运行方式：python3 python_lists_dicts_demo.py
"""


def main():
    print("========== 一、列表 list（≈ C 的动态数组） ==========")

    # ============ 1. 创建：元素类型可以混搭 ============
    # C 语言：int arr[3] = {1, 2, 3};  数组元素必须是同一类型
    # Python：列表里可以装任何类型（存的是"引用"）
    lst = [1, "apple", 3.14, True]
    print("1) 创建列表(异构):", lst)

    # ============ 2. 动态长度：append 自动扩容 ============
    # C 语言：数组长度固定，要扩容得自己 malloc/realloc
    # Python：append 末尾追加，自动管理内存
    nums = []
    nums.append(10)
    nums.append(20)
    nums.append(30)
    print("2) append 追加:", nums, " 长度 len =", len(nums))

    # ============ 3. 索引与负索引 ============
    # C 语言：arr[i]，没有负索引
    # Python：lst[-1] 倒数第一个
    t = [10, 20, 30, 40, 50]
    print("3) t[0] =", t[0], " t[-1] =", t[-1], " t[-2] =", t[-2])

    # ============ 4. 切片：返回新列表 ============
    # C 语言：要手动复制一部分元素
    print("4) t[1:3] =", t[1:3], "(左闭右开，和字符串一样)")

    # ============ 5. 插入与删除 ============
    # C 语言：插入要 memmove 挪动后续元素；删除要循环移位，很繁琐
    # Python：insert/pop/remove/del 一行搞定
    s = [1, 2, 4]
    s.insert(2, 3)      # 在下标 2 处插入 3
    print("5) insert 后:", s)
    last = s.pop()      # 弹出末尾
    print("   pop 弹出:", last, " 剩余:", s)
    s.remove(2)         # 按值删除第一个 2
    print("   remove(2) 后:", s)
    del s[0]            # 按下标删除
    print("   del s[0] 后:", s)

    # ============ 6. 成员判断与查找下标 ============
    # C 语言：要手写循环逐个比较
    # Python：x in lst / lst.index(x) 内置
    colors = ["red", "green", "blue"]
    print("6) 'green' in colors:", "green" in colors)
    print("   colors.index('blue') =", colors.index("blue"))

    # ============ 7. 排序与反转 ============
    # C 语言：qsort 需要自己写比较函数和元素大小
    # Python：sort() 就地排序，sorted() 返回新列表
    numbers = [5, 2, 8, 1, 9]
    numbers.sort()
    print("7) sort 后:", numbers)
    numbers.reverse()
    print("   再 reverse 后:", numbers)

    # ============ 8. 遍历 ============
    # C 语言：for (i = 0; i < n; i++) printf("%d", arr[i]);
    # Python：for x in lst 直接拿元素
    for x in [1, 2, 3]:
        print("8) 遍历元素:", x)

    # ============ 9. 拼接与复制 ============
    # C 语言：拼接要 memcpy 到新缓冲区；复制用 memcpy
    # Python：+ 拼接；lst[:] 浅复制（复制了引用，不是深层拷贝）
    a = [1, 2]
    b = [3, 4]
    print("9) a + b =", a + b, " a * 2 =", a * 2)
    copy_a = a[:]       # 浅拷贝：新列表，但元素引用相同
    print("   a[:] 复制 =", copy_a)

    # ============ 10. 列表推导式 ============
    # C 语言：先建数组，再 for 循环逐个算
    # Python：一行生成新列表 [表达式 for 元素 in 序列 if 条件]
    squares = [x * x for x in range(6)]
    even = [x for x in range(10) if x % 2 == 0]
    print("10) 推导式:", squares, " 偶数:", even)

    # ============ 11. 可变对象：函数内修改外部可见 ============
    # C 语言：传数组名（退化为指针）才能改外部数组
    # Python：列表是可变对象，直接传引用（回顾第 12 节）
    def add_tail(lst):
        lst.append(99)

    demo = [1, 2]
    add_tail(demo)
    print("11) 函数内 append 后:", demo)

    # ============ 12. 多维列表（矩阵） ============
    # C 语言：int m[2][3] = {{1,2,3},{4,5,6}};
    # Python：列表套列表
    matrix = [[1, 2, 3], [4, 5, 6]]
    print("12) 二维列表:", matrix, " matrix[1][2] =", matrix[1][2])

    print()
    print("========== 二、字典 dict（C 里没有，对应哈希表） ==========")

    # ============ 13. 创建 ============
    # C 语言：没有内置字典；通常用结构体数组 + 线性查找，或用哈希表库
    # Python：{键: 值}，键值对映射
    person = {"name": "小明", "age": 18, "city": "成都"}
    print("13) 创建字典:", person)

    # ============ 14. 访问与 get ============
    # C 语言：数组下标越界是未定义行为，要自己先判断
    # Python：d[key] 不存在会报 KeyError；get() 不报错返回默认值
    print("14) person['name'] =", person["name"])
    print("    person.get('job') =", person.get("job"),
          " get('job', '未知') =", person.get("job", "未知"))

    # ============ 15. 新增/修改：key 不存在自动新增 ============
    # C 语言：要自己处理"存在则更新，不存在则插入"
    person["job"] = "程序员"     # key 不存在 → 新增
    person["age"] = 19           # key 已存在 → 覆盖
    print("15) 新增/修改后:", person)

    # ============ 16. 删除 ============
    # C 语言：哈希表删除/结构体数组标记删除
    # Python：del / pop
    removed = person.pop("city")
    print("16) pop('city') 弹出:", removed, " 剩余:", person)

    # ============ 17. 判断 key 是否存在 ============
    # C 语言：线性查找自己写循环
    # Python：key in d
    print("17) 'name' in person:", "name" in person,
          " 'city' in person:", "city" in person)

    # ============ 18. 遍历 ============
    # C 语言：遍历结构体数组
    # Python：items() 同时拿 key 和 value
    for k, v in person.items():
        print("18) 键值对:", k, "=", v)

    # ============ 19. key 必须是不可变类型 ============
    # C 语言：结构体/数组都能当键（自己写比较逻辑）
    # Python：key 必须是可哈希的不可变类型（int/str/tuple）
    d = {1: "整数键", "str": "字符串键", (1, 2): "元组键"}
    print("19) 各种 key:", d)
    # d[[1, 2]] = "x"  ← 报错 TypeError: unhashable type: 'list'
    print("    列表不能做 key（列表可变，无法哈希）")

    # ============ 20. 典型用法：统计字符频率 ============
    # C 语言：要开数组或手写哈希
    # Python：字典计数一行思维
    text = "hello"
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    print("20) 字符频率:", freq)


if __name__ == "__main__":
    main()
#（注：内容由AI生成）
