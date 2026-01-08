# GenerarTree

Este script genera una representación en árbol de la estructura de directorios de una carpeta especificada y la guarda en un archivo de texto.

## Archivo Python: `generar_tree.py`

### Descripción
El script recorre recursivamente la carpeta base hasta una profundidad máxima especificada, creando una estructura visual en formato de árbol ASCII. La salida se guarda en `estructura.txt`.

### Requisitos
- Python 3.x
- Módulo `os` (incluido en la instalación estándar de Python)

### Configuración
Antes de ejecutar, modifica la variable `base_path` con la ruta absoluta de la carpeta que deseas documentar:
```python
base_path = r"ruta\a\tu\carpeta"
```

Opcionalmente, ajusta `max_depth` para limitar la profundidad del árbol (por defecto: 6).

### Ejecución
Ejecuta el script desde la línea de comandos:
```
python generar_tree.py
```

### Salida
- Archivo `estructura.txt` con la estructura del directorio en formato de árbol.
- Mensaje en consola confirmando la generación del archivo.

### Ejemplo de salida
```
carpeta_base/
├── subcarpeta1/
│   ├── archivo1.txt
│   └── archivo2.txt
└── subcarpeta2/
    └── archivo3.txt
```