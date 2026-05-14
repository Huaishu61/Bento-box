# core_engine.py (底层引擎：负责所有具体的执行逻辑)
import os
import glob

def get_file_contents(directory_path, extension="*.html"):
    """
    通用函数：顺次读取指定文件夹下所有指定后缀的文件内容。
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"⚠️ 自动创建了缺失的文件夹：{os.path.basename(directory_path)}")
        return ""

    file_paths = sorted(glob.glob(os.path.join(directory_path, extension)))
    blocks = [open(f, "r", encoding="utf-8").read().strip() for f in file_paths]
    
    # 用回车符连接所有读取到的代码块
    return "\n\n".join(blocks)


def assemble_html(modules_content, widgets_content, output_file):
    """
    通用函数：将读取到的碎片内容注入到 HTML 底座模板中。
    """
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
        {modules_content}
    </div>

    {widgets_content}

</body>
</html>"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(base_template)
    
    print("🚀 空间站对接完成！")
    print(f"📍 主页已刷新：{output_file}")