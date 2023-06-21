import os

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))

# Beispielaufruf
directory_path = "docs/DUP"
list_files(directory_path)
