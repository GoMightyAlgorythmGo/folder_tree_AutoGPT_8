import os
from pathlib import Path

def generate_tree_html(path):
    html = '<ul class="tree-view">'
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            html += f'<li>{item}</li>'
        elif os.path.isdir(item_path):
            html += f'<li class="folder">{item}</li>{generate_tree_html(item_path)}'
    html += '</ul>'
    return html

def write_files(tree_html):
    with open('index.html', 'w') as f:
        f.write(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>File and Folder Tree</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
{tree_html}
<script src="script.js"></script>
</body>
</html>''')

    with open('style.css', 'w') as f:
        f.write('''ul, li {
    list-style-type: none;
    padding-left: 20px;
}

.tree-view ul {
    display: none;
}

.tree-view ul.visible {
    display: block;
}

.folder {
    cursor: pointer;
}''')

    with open('script.js', 'w') as f:
        f.write('''document.addEventListener('DOMContentLoaded', function () {
    let folders = document.querySelectorAll('.folder');
    
    folders.forEach(folder => {
        folder.addEventListener('click', function () {
            let subTree = this.nextElementSibling;
            subTree.classList.toggle('visible');
        });
    });
});''')

if __name__ == '__main__':
    folder_path = 'C:\\Programming\\Auto-GPT_AI_8\\auto_gpt_workspace'  # Replace with your folder path
    tree_html = generate_tree_html(folder_path)
    write_files(tree_html)
