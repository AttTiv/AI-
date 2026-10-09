# -*- coding: utf-8 -*-
"""
Python 字符串用法入门示例 —— 面向有 C 语言基础的读者
=====================================================
每个小节都标注了与 C 语言的对应/差异点。
运行方式：python3 python_strings_demo.py
"""


def main():
    # ============ 1. 创建：单引号 / 双引号都行 ============
    # C 语言：char s[] = "hello";  只能用双引号
    # Python：'hello' 和 "hello" 完全等价；三引号 ''' 或 """ 可写多行
    s1 = 'hello'
    s2 = "world"
    s3 = """第一行
第二行"""
    print("1) 创建:", s1, s2)
    print("   多行字符串:", repr(s3))

    # ============ 2. 不可变：不能改单个字符 ============
    # C 语言：char s[] = "hello"; s[0] = 'H';  ← 可以修改
    # Python：字符串一旦创建就不可变，改单个字符会报错
    s = "hello"
    # s[0] = 'H'  ← 报错 TypeError: 'str' object does not support item assignment
    print("2) 字符串不可变: s =", s, "(想改只能新建一个字符串)")
    s_new = 'H' + s[1:]
    print("   新建后: s_new =", s_new)

    # ============ 3. 索引与切片 ============
    # C 语言：s[i] 取第 i 个 char；没有负索引、没有切片
    # Python：s[0] 第一个，s[-1] 倒数第一个，s[1:4] 切片，s[::-1] 反转
    t = "abcdef"
    print("3) t =", t)
    print("   t[0] =", t[0], " t[-1] =", t[-1], " t[1:4] =", t[1:4])
    print("   t[::-1] =", t[::-1], "(反转，C 里要手写循环)")

    # ============ 4. 拼接与重复 ============
    # C 语言：strcat(dst, src) 必须保证 dst 缓冲区够大，否则越界
    # Python：+ 直接拼接（自动分配内存），* 重复
    a = "Py"
    b = "thon"
    print("4) 拼接:", a + b, " 重复:", a * 3)

    # ============ 5. 长度 ============
    # C 语言：strlen(s) 要数到 '\0'，O(n)
    # Python：len(s) 直接返回，O(1)（字符串内部自带长度）
    print("5) len('hello') =", len("hello"))

    # ============ 6. 比较：== 比内容！ ============
    # C 语言：比内容要用 strcmp(s1, s2) == 0；s1 == s2 比较的是指针地址（坑！）
    # Python：== 直接比较内容，天然安全
    x = "abc"
    y = "abc"
    print("6) 'abc' == 'abc':", x == y, "(C 里 x == y 通常是在比地址)")

    # ============ 7. 查找子串 ============
    # C 语言：strstr(s, "lo") 返回指针，找不到返回 NULL
    # Python："lo" in s 返回布尔；s.find("lo") 返回下标，找不到返回 -1
    txt = "hello world"
    print("7) 'lo' in txt:", "lo" in txt)
    print("   txt.find('lo') =", txt.find("lo"), " txt.find('zz') =", txt.find("zz"))

    # ============ 8. 大小写转换 ============
    # C 语言：要手动循环调用 toupper()/tolower()
    # Python：upper()/lower() 一行搞定
    print("8) 'Hello'.upper() =", "Hello".upper(),
          "  .lower() =", "Hello".lower())

    # ============ 9. 分割与合并 ============
    # C 语言：strtok(s, ",") 会破坏原字符串且不可重入
    # Python：split() 返回新列表，原字符串不变；join() 反向合并
    data = "apple,banana,cherry"
    parts = data.split(",")
    print("9) split:", parts)
    print("   join:", " | ".join(parts))   # C 里要手写循环拼

    # ============ 10. 去除空白 ============
    # C 语言：手动循环判断 isspace
    # Python：strip() 去掉首尾空白
    messy = "  hello  "
    print("10) strip:", repr(messy.strip()), "(去掉首尾空格)")

    # ============ 11. 替换 ============
    # C 语言：标准库没有替换函数，要自己写循环
    print("11) replace:", "hello".replace("l", "L"))

    # ============ 12. 格式化 f-string ============
    # C 语言：printf("%s 今年 %d 岁", name, age) / sprintf
    # Python：f"..." 直接在字符串里嵌表达式（Python 3.6+）
    name = "小明"
    age = 18
    print(f"12) f-string: {name} 今年 {age} 岁")

    # ============ 13. Unicode：一个 str = 任意字符 ============
    # C 语言：char 单字节，中文要 wchar_t 或 UTF-8 字节处理
    # Python：str 直接存字符，中文就是一个字符
    cn = "你好，世界"
    print("13) 中文:", cn, " len =", len(cn), "(一个汉字算一个字符)")

    # ============ 14. 遍历：直接 for ch in s ============
    # C 语言：for (i = 0; s[i] != '\0'; i++) 逐个取
    # Python：for 循环直接拿每个字符
    for ch in "abc":
        print("14) 遍历字符:", ch)

    # ============ 15. 判断方法 ============
    # C 语言：isdigit(c) / isalpha(c) 判断单个 char
    # Python：整串判断 isdigit() / isalpha() / isalnum()
    print("15) '123'.isdigit() =", "123".isdigit(),
          " 'ab'.isalpha() =", "ab".isalpha(),
          " '12ab'.isalnum() =", "12ab".isalnum())

    # ============ 16. 原始字符串 r"..." ============
    # C 语言：路径里的反斜杠要写两个 "C:\\temp\\file"
    # Python：r"..." 里 \ 就是 \，写路径/正则表达式超方便
    path = r"C:\temp\file.txt"
    print("16) 原始字符串:", path)


if __name__ == "__main__":
    main()
#（注：内容由AI生成）
