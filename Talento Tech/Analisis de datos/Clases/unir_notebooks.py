import subprocess

# Definir el comando para unir los notebooks
command = [
    'nbmerge',
    '1- Python basics.ipynb', '2- Análisis de Medidas Estadísticas.ipynb'
]

# Ejecutar el comando y capturar la salida en UTF-8
process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')

# Escribir la salida capturada en el archivo con codificación UTF-8
with open('notebook_combinado.ipynb', 'w', encoding='utf-8') as output_file:
    output_file.write(process.stdout)

# Mostrar errores si ocurren
if process.stderr:
    print("Error:", process.stderr)