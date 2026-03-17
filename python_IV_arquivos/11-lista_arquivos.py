import glob, os, zipfile

# 1 - Diretório de trabalho atual
os.getcwd()

# 2 - Listar todos os arquivos .txt
for file in glob.glob('*.txt'):
    print(file)

# 3  - Todos os arquivos .csv
for file in glob.glob('*.csv'):
    print(file)

# 4 - Compactar arquivos .txt em um arquivo zip
with zipfile.ZipFile('names.zip', 'w') as zip_file:
    for file in glob.glob('*.txt'):
        zip_file.write(file)

# 5 - Compactar arquivo csv em um arquivo zip
with zipfile.ZipFile('courses.zip', 'w') as zip_file:
    for file in glob.glob('*.csv'):
        zip_file.write(file)

# 6 - Comactar todos os arquivos .txt e .csv em um arquivo zip
with zipfile.ZipFile('all_files.zip', 'w') as zip_file:
    for file in glob.glob('*.txt'):
        zip_file.write(file)