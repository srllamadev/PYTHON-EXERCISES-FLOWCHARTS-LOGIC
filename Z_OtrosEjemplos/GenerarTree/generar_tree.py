import os

# Ruta base que quieres documentar
'''
Coloca la direccion de la carpeta que quieres documentar.
'''
base_path = r"direccion_carpeta"

# Profundidad máxima
max_depth = 3

# Archivo de salida
output_file = "estructura.txt"

def tree(dir_path, prefix="", depth=0, max_depth=3, file_handle=None):
    if depth > max_depth:
        return

    items = sorted(os.listdir(dir_path))
    for index, item in enumerate(items):
        path = os.path.join(dir_path, item)
        connector = "└── " if index == len(items) - 1 else "├── "
        file_handle.write(f"{prefix}{connector}{item}\n")

        if os.path.isdir(path) and depth < max_depth - 1:
            extension = "    " if index == len(items) - 1 else "│   "
            tree(path, prefix + extension, depth + 1, max_depth, file_handle)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"{os.path.basename(base_path)}/\n")
    tree(base_path, "", 1, max_depth, f)

print(f"Estructura guardada en {output_file}")
