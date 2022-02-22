# README

## Angular

 1. Crear un nuevo proyecto en angular, Ng new ("El nombre del nuevo directorio").
 2. Copiar datos necesarios enviados.
 3. Entrar en VScode o en una libreria y ejecutarlo en ng serve -o.

## Python

## Selenium

## Pandas
Importamos panda mediante el 
>import pandas as pd

## Creación de csv con python
```python
import csv 
with open('ejemplo.csv', 'w') as csvfile:
   fieldnames = ['filtro1', 'filtro2', 'filtro3']
   writer  = csv.DictWriter(csvfile, fieldnames = fieldnames)
   writer.writeheader()
   writer.writerow({'filtro1' : 'Marta','filtro2' : 'Marco', 'filtro3' : 'Marso'})

print("datos insertados")
```

## Bibliografía

[Leer csv](https://pharos.sh/leer-y-escribir-archivos-csv-en-python-con-pandas/)
