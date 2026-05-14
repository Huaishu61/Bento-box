import os
import glob

def build_station():
    # --- 1. 定位逻辑 ---
    base_dir = os.path.dirname(os.path.abspath(__file__))
    modules_dir = os.path.join(base_dir, "modules")
    widgets_dir = os.path.join(base_dir, "widgets")
    output_file = os.path.join(base_dir, "index.html")

    # 确保必需的文件夹存在
    for directory in [modules_dir, widgets_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"⚠️ 自动创建了缺失的文件夹：{os.path.basename(directory)}")

    # --- 2. 读取网格模块 (modules) ---
    module_files = sorted(glob.glob(os.path.join(modules_dir, "*.html")))
    bento_blocks = [open(f, "r", encoding="utf-8").read().strip() for f in module_files]
    all_blocks_html = "\n\n        \n        ".join(bento_blocks)

    # --- 3. 读取悬浮插件 (widgets) ---
    widget_files = sorted(glob.glob(os.path.join(widgets_dir, "*.html")))
    widget_blocks = [open(f, "r", encoding="utf-8").read().strip() for f in widget_files]
    all_widgets_html = "\n\n    \n    ".join(widget_blocks)

    # --- 4. 组装空间站 (极致纯净的 HTML 骨架) ---
    base_template = f"""<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>空间站 | 数字化主页</title>
    <link rel="stylesheet" href="./style.css">
</head>
<body>
    
    <nav class="navbar">
        <div class="nav-container">
            <span class="nav-title">🚀 空间站</span>
            <div class="nav-links">
                <a href="#">🏠 首页</a>
                <a href="#">🔬 实验室</a>
                <a href="#">📦 资源舱</a>
                <a href="#">✉️ 联络</a>
            </div>
        </div>
    </nav>

    <div class="bento-grid">
        {all_blocks_html}
    </div>

    {all_widgets_html}

</body>
</html>"""

    # --- 5. 生成最终主页 ---
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(base_template)
    
    print("🚀 空间站对接完成！")
    print(f"📦 组装了 {len(module_files)} 个核心方块。")
    print(f"🧩 挂载了 {len(widget_files)} 个悬浮插件。")
    print(f"📍 主页已刷新：{output_file}")

if __name__ == "__main__":
    build_station()