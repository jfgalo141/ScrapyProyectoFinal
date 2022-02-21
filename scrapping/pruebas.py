diccionario={
    "juan":{"juanes":"juanito"},
    "manolo":{"manolos":"manolito"}
}

filtros = {"juan":"juanes"}

for i in filtros:
    print(str(i)+str(diccionario[i])+str(diccionario[i][filtros[i]]))