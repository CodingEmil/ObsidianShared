import os
import re

def replace_code_blocks(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    pattern = r'``` ad-.*?\n(.*?)```'
    updated_content = re.sub(pattern, r'!!! note\n\1', content, flags=re.DOTALL)

    with open(file_path, 'w') as f:
        f.write(updated_content)

def replace_code_blocks_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                replace_code_blocks(file_path)

# Beispielaufruf
directory_path = "docs"

replace_code_blocks_in_directory(directory_path)
