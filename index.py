import pdfplumber
import pandas as pd
import os
import json

def extract_tables_from_pdf(filename):
    """
    Extract tables from a PDF file using pdfplumber.

    Parameters
    ----------
    filename : str
        The path to the PDF file from which to extract tables.

    Returns
    -------
    list of lists or None
        Returns a list of tables, where each table is a list of lists containing
        the table data extracted from each page of the PDF. If an error occurs
        during the PDF processing, returns None.
    """
    tables = []
    try:
        with pdfplumber.open(filename) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    tables.append(table)
        return tables
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        return None

def save_tables_as_json(tables, json_filename):
    """
    Saves all tables extracted from a PDF file to a JSON file.

    Parameters
    ----------
    tables : list of lists
        Each sublist represents a table in the PDF file. The first item in each
        sublist is a list of column headers, and the remaining items are the rows
        of the table, where each row is a list of values.
    json_filename : str
        The filename of the JSON file to save the tables to.

    Returns
    -------
    None
    """
    all_tables = []

    
    for i, table in enumerate(tables):
        header = table[0]  
        data = table[1:]  
        df = pd.DataFrame(data, columns=header)
        table_dict = df.to_dict(orient='records')
        all_tables.append({
            'table_number': i + 1,
            'table_data': table_dict
        })

    
    with open(json_filename, 'w', encoding='utf-8') as jsonf:
        json.dump(all_tables, jsonf, ensure_ascii=False, indent=4)
    print(f"Todas las tablas guardadas en {json_filename}")

def format_text(json_filename):
    """
    Read a JSON file, perform some text replacements and write it back to the same file.
    
    Replacements:
        - lowercase
        - accented vowels replaced with their unaccented counterparts
        - "mar-29" replaced with "mar 29"
        - "mierc 30" replaced with "mier 30"
        - newlines and hyphens replaced with spaces
        - "ssaabb 0021" and "ssaabb 0 021" replaced with "sab 02"
    
    :param json_filename: the name of the JSON file to read and write
    """

    with open(json_filename, "r" , encoding="utf-8") as jsonf:
    
        data = jsonf.read()
        data = data.lower()
        data = data.replace("á", "a")
        data = data.replace("é", "e")
        data = data.replace("í", "i")
        data = data.replace("ó", "o")
        data = data.replace("ú", "u")
        data = data.replace("mar-29", "mar 29")
        data = data.replace("mierc 30", "mier 30")
        data = data.replace(r"-\n", '')
        data = data.replace(r"\n", ' ')
        data = data.replace("ssaabb 0021", "sab 02")
        data = data.replace("ssaabb 0 021", "sab 02")
        print(type(data))

    with open(json_filename, "w", encoding="utf-8") as jsonf:
        jsonf.write(data)


if __name__ == "__main__":
    pdf_filename = r"./files/example.pdf"  
    tables = extract_tables_from_pdf(pdf_filename)
    
    if tables:
        print(tables)
        json_filename = os.path.splitext(pdf_filename)[0] + ".json"
        save_tables_as_json(tables, json_filename)
        format_text(json_filename)
    else:
        print("No se encontraron tablas en el archivo PDF.")