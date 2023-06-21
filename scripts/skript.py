import os

def replace_text_in_files(directory, file_extension, search_text, replace_text):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                if search_text in content:
                    content = content.replace(search_text, replace_text)
                    with open(file_path, 'w') as f:
                        f.write(content)
                        print(f"Text ersetzt in Datei: {file_path}")

# Beispielaufruf
directory_path = "/pfad/zum/verzeichnis"
file_extension = ".md"
search_text = "title: Ziel-MAC (Punkt-zu-Punkt)\nGibt den nächsten Host an, den ein Paket erreichen soll (Punkt-zu-Punkt)"
replace_text = "!!! note\ntitle: Ziel-MAC (Punkt-zu-Punkt)\nGibt den nächsten Host an, den ein Paket erreichen soll (Punkt-zu-Punkt)"

replace_text_in_files(directory_path, file_extension, search_text, replace_text)
