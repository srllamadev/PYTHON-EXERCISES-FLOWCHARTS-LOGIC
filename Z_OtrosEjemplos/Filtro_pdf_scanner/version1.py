import fitz  # PyMuPDF
import cv2
import numpy as np
from PIL import Image
import os

def enhance_scan_effect(image):
    # Convertir a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar suavizado para quitar ruido
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Aumentar contraste (efecto de escaneo)
    _, scanned = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return scanned

def pdf_to_scanned(input_pdf_path, output_pdf_path):
    doc = fitz.open(input_pdf_path)
    scanned_images = []

    for page_number in range(len(doc)):
        # Renderizar página a imagen
        pix = doc.load_page(page_number).get_pixmap(dpi=300)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Convertir PIL a OpenCV
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Aplicar filtro de escáner
        scanned_img = enhance_scan_effect(img_cv)

        # Convertir de nuevo a PIL
        final_img = Image.fromarray(scanned_img)

        # Guardar temporalmente la imagen procesada
        temp_img_path = f"page_{page_number}.png"
        final_img.save(temp_img_path)
        scanned_images.append(temp_img_path)

    # Guardar imágenes como PDF final
    images = [Image.open(img).convert('RGB') for img in scanned_images]
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])

    # Limpiar archivos temporales
    for img in scanned_images:
        os.remove(img)

    print(f"✅ PDF procesado guardado en: {output_pdf_path}")

# 👉 Uso:
pdf_to_scanned("entrada.pdf", "salida_escaneada.pdf")
