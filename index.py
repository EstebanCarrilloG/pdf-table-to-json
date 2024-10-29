import pdfplumber
import pandas as pd
import os
import json

def extract_tables_from_pdf(filename):
    tables = []
    try:
        with pdfplumber.open(filename) as pdf:
            for page in pdf.pages:
                # Extract table assuming tables with borders
                table = page.extract_table()
                if table:
                    tables.append(table)
        return tables
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        return None

def save_tables_as_json(tables, json_filename):
    # Lista para almacenar las tablas en formato JSON
    all_tables = []

    # Convertir cada tabla extraída en un DataFrame de pandas y luego a diccionario
    for i, table in enumerate(tables):
        header = table[0]  # La primera fila como encabezado
        data = table[1:]  # El resto de las filas como datos
        df = pd.DataFrame(data, columns=header)  # Convertir en DataFrame
        
        # Convertir DataFrame a lista de diccionarios
        table_dict = df.to_dict(orient='records')
        all_tables.append({
            'table_number': i + 1,
            'table_data': table_dict
        })

    # Guardar todas las tablas en un solo archivo JSON
    with open(json_filename, 'w', encoding='utf-8') as jsonf:
        json.dump(all_tables, jsonf, ensure_ascii=False, indent=4)
    print(f"Todas las tablas guardadas en {json_filename}")

if __name__ == "__main__":
    # Step 1: Extract tables from PDF
    pdf_filename = r"./files/Tungurahua-desconexiones-del-28-al-30-de-octubre.pdf"  # Reemplaza con tu archivo PDF
    tables = extract_tables_from_pdf(pdf_filename)
    
    if tables:
        # Step 2: Save all tables into a single JSON file
        json_filename = os.path.splitext(pdf_filename)[0] + ".json"
        save_tables_as_json(tables, json_filename)
    else:
        print("No se encontraron tablas en el archivo PDF.")