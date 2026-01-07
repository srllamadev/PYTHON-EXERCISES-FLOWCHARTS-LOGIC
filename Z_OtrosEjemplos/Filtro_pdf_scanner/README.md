# Filtro PDF Scanner - Version 1

Este script en Python convierte un PDF normal en una versión que simula un documento escaneado, aplicando filtros de imagen para darle un aspecto de escaneo.

## Funcionalidades
- Convierte páginas de PDF a imágenes de alta resolución (300 DPI).
- Aplica efectos de escaneo: conversión a escala de grises, suavizado, y umbralización para simular un escáner.
- Genera un nuevo PDF con las páginas procesadas.

## Requisitos
- PyMuPDF (fitz)
- OpenCV (cv2)
- NumPy
- Pillow (PIL)

Instala las dependencias con: `pip install PyMuPDF opencv-python numpy pillow`

## Uso
Ejecuta el script con:
```python
python version1.py
```
Asegúrate de modificar las rutas de entrada y salida dentro del script.

## Autor
Versión 1 - Script básico para simular escaneo de PDFs.