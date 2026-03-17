import csv

name= input('Informe o nome da linguagem que deseja aprender:')
category = input('Informe a categoria da linguagem:')

with open('courses.csv', 'a', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow([name, category])