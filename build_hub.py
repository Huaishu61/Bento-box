import os
import glob

def build_station():
    # --- 1. 定义空间站路径 ---
    base_dir = os.path.dirname(os.path.abspath(__file__))
    modules_dir = os.path.join(base_dir, "modules")
    output_file = os.path.join(base_dir, "index.html")

    # 确保模块文件夹存在
    if not os.path.exists(modules_dir):
        os.makedirs(modules_dir)
        print("⚠️ 未找到 modules 文件夹，已自动创建。请把你的方块HTML放进去！")
        return

    # --- 2. 顺次读取模块碎片 ---
    # 获取所有 .html 文件，并按文件名排序（保证 01, 02, 03 的顺序）
    module_files = sorted(glob.glob(os.path.join(modules_dir, "*.html")))
    
    bento_blocks = []
    for file_path in module_files:
        with open(file_path, "r", encoding="utf-8") as f:
            bento_blocks.append(f.read().strip())
    
    # 将所有方块代码合并成一整段 HTML
    all_blocks_html = "\n\n        \n        ".join(bento_blocks)

    # --- 3. 准备空间站底座 (HTML 骨架) ---
    # 注意这里通过 <link> 引入了独立的 style.css
    base_template = f"""<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的数字名片 | 空间站中转舱</title>
    <link rel="stylesheet" href="./style.css">
</head>
<body>
    <div class="bento-grid">
        {all_blocks_html}
        </div>
</body>
</html>"""

    # --- 4. 生成最终主页 ---
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(base_template)
    
    print("🚀 空间站对接完成！")
    print(f"📦 共组装了 {len(module_files)} 个模块。")
    print(f"📍 主页已刷新：{output_file}")

if __name__ == "__main__":
    build_station()