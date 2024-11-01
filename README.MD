# PDF Table to JSON Formatter

This Python script extracts tables from PDF files, converts them into JSON format, and formats the JSON text for improved readability. It is particularly useful for processing tabular data from PDFs for analysis and reporting.

## Features

- Extracts tables from PDF files using `pdfplumber`
- Converts extracted tables into JSON format with clear structure
- Formats JSON text by performing various text replacements and cleaning

## Requirements

- Python 3.x
- `pdfplumber` - for PDF data extraction
- `pandas` - for handling tabular data
- `json` (built-in) - for JSON data manipulation

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/pdf-table-to-json.git
   cd pdf-table-to-json
   ```

2. Install dependencies:
   ```bash
   pip install pdfplumber pandas
   ```
## Usage

1. Place the PDF file in the files folder (or specify your own path).

2. Run the script:
   ```bash
   python pdf_to_json_formatter.py
   ```
3. The JSON output will be saved in the same directory as the PDF file with the same name but with a .json extension.

## Example
If you run the script with a PDF file containing tables, it will extract the tables and save the JSON output. The JSON file will look something like this:

```json
[
  {
    "table_number": 1,
    "table_data": [
      {
        "Column 1": "Value 1",
        "Column 2": "Value 2"
      },
      {
        "Column 1": "Value 3",
        "Column 2": "Value 4"
      }
    ]
  },
  {
    "table_number": 2,
    "table_data": [
      {
        "Column 1": "Value 5",
        "Column 2": "Value 6"
      }
    ]
  }
]
```
## Text Formatting
The script also performs text replacements in the JSON output file.

### Example:
* Converts text to lowercase
* Replaces accented vowels with unaccented counterparts
* Replaces "mar-29" with "mar 29"
* Replaces "mierc 30" with "mier 30"
* Removes newlines and hyphens, replacing them with spaces
* Replaces "ssaabb 0021" and "ssaabb 0 021" with "sab 02"

## Configuration
You can customize the input PDF filename in the **pdf_filename** variable within the script.
