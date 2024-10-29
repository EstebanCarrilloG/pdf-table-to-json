import json

file_name = "./files/Tungurahua-desconexiones-del-28-al-30-de-octubre-copy.json"


with open(file_name, "r" , encoding="utf-8") as jsonf:
    data = jsonf.read()
    data = data.lower()
    data = data.replace("á", "a")
    data = data.replace("é", "e")
    data = data.replace("í", "i")
    data = data.replace("ó", "o")
    data = data.replace("ú", "u")
    data = data.replace("mar-29", "mar 29")
    data = data.replace("mierc 30", "mier 30")
    data = data.replace("-\n", "")
    print(data)

with open(file_name, "w", encoding="utf-8") as jsonf:
    jsonf.write(data)
