import fitz  # PyMuPDF
import re


# Ruta al archivo PDF
pdf_path = '/PATH/TO/YOUR/PDF_FILE/EXTRACT.pdf'

# Abrir el archivo PDF
pdf_document = fitz.open(pdf_path)

# Extraer texto de cada página
text = ""
for page_num in range(len(pdf_document)):
    page = pdf_document.load_page(page_num)
    text += page.get_text()

# Cerrar el documento PDF
pdf_document.close()

# Buscar todas las transacciones de Uber o Didi y sus montos
matches = re.findall(r'(UBER|DIDI)[^\$]*\$([\d,]+\.\d{2})', text)

# Convertir los montos a números y sumarlos
total_transport = sum(float(amount.replace(',', '')) for _, amount in matches)

print(f"Total gastado en transporte: ${total_transport:.5f}")

