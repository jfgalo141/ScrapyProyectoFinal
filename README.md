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

## Lectura de csv con python
```python
import csv
with open('ejemplo.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)
```

## Actualizar datos de csv con python usando pandas

```python
import pandas as pd 

df = pd.read_csv("ejemplo.csv") 
df.loc[5, 'filtro1'] = 'Sandra'
df.to_csv("ejemplo.csv", index=False) 
print(df)
```



## Bibliografía
[Leer csv](https://pharos.sh/leer-y-escribir-archivos-csv-en-python-con-pandas/)
[Actualizar csv](https://es.acervolima.com/actualizar-el-valor-de-la-columna-de-csv-en-python/)
[]

