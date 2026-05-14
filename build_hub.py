# build_hub.py (主控台：只负责定义路径和调用引擎)
import os

# 从我们的“头文件” (模块) 中引入功能函数
from core_engine import get_file_contents, assemble_html

def main():
    # 1. 定义空间站的各个舱室路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    modules_dir = os.path.join(base_dir, "modules")
    widgets_dir = os.path.join(base_dir, "widgets")
    output_file = os.path.join(base_dir, "index.html")

    # 2. 调用引擎：读取碎片
    print("正在扫描舱室...")
    modules_html = get_file_contents(modules_dir)
    widgets_html = get_file_contents(widgets_dir)

    # 3. 调用引擎：组装并生成最终网页
    print("开始执行组装协议...")
    assemble_html(modules_html, widgets_html, output_file)

if __name__ == "__main__":
    main()