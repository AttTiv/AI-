import os, subprocess, urllib.parse, sys

BASE = r"E:\workbuddy workspace"
OUT = os.path.join(BASE, "corpus_pdf")
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

FILES = [
    ("新国标大点位控制器_缺陷闭环系统_方案建议书_v1.4.html", "01_方案建议书_v1.4"),
    ("新国标大点位控制器_缺陷闭环系统_方案建议书_v1.2.html", "02_方案建议书_v1.2_旧版"),
    ("缺陷闭环系统_字段填写顺序与依赖图.html", "03_字段填写顺序与依赖图"),
    ("缺陷闭环系统_45字段全流程图.html", "04_45字段全流程图"),
    ("缺陷闭环系统_字段配置器.html", "05_字段配置器"),
    ("缺陷闭环系统_智能表格建表作业单_v2.html", "06_建表作业单_v2"),
    ("缺陷闭环系统_企微表单建表作业单_v1.html", "07_企微表单建表作业单_v1"),
    ("任务拆分_交接卡.html", "08_任务拆分_交接卡"),
    ("硬件技能调用速查卡.html", "09_硬件技能调用速查卡"),
    ("硬件技能安装验收报告.html", "10_硬件技能安装验收报告"),
    ("Anthropic官方文档_中文精读.html", "11_Anthropic文档中文精读"),
    ("AI嵌入式软硬件新闻周报_2026-10-17.html", "12_新闻周报_2026-10-17"),
    ("AI嵌入式软硬件新闻周报_2026-10-24.html", "13_新闻周报_2026-10-24"),
    ("AI嵌入式软硬件新闻周报_2026-10-31.html", "14_新闻周报_2026-10-31"),
    ("AI工程师三个月学习计划.html", "15_AI学习计划"),
    ("W4_RAG入门_五环节与检索实验.html", "16_W4_RAG教程"),
]

ok, fail = [], []
for src, name in FILES:
    path = os.path.join(BASE, src)
    if not os.path.exists(path):
        fail.append((src, "源文件不存在"))
        continue
    url = "file:///" + urllib.parse.quote(path.replace("\\", "/"))
    dst = os.path.join(OUT, name + ".pdf")
    r = subprocess.run([EDGE, "--headless=old", "--disable-gpu", "--no-pdf-header-footer",
                        "--print-to-pdf=" + dst, url],
                       capture_output=True, timeout=120)
    if os.path.exists(dst) and os.path.getsize(dst) > 20000:
        ok.append((name, round(os.path.getsize(dst) / 1024)))
    else:
        fail.append((src, "转换失败 r=%s" % r.returncode))

print("成功 %d 个：" % len(ok))
for n, kb in ok:
    print("  %-36s %6d KB" % (n, kb))
if fail:
    print("失败 %d 个：" % len(fail))
    for n, why in fail:
        print("  ", n, why)
total = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT) if f.endswith(".pdf"))
print("合计 %.1f MB" % (total / 1024 / 1024))
