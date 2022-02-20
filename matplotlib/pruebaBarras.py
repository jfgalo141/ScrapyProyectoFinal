import matplotlib.pyplot as plt
#Valores eje y (El maximo es el mas alto y el mas bajo  es el menor )
y=[500,800,600,1000,650]
#Cantidad de valores de x(debe de haber la misma cantidad de x y de y)
x=[1,2,3,4,5]
#Pasar de numero a texto (No lo he probado con el eje y)
x_text=["SQL","JavaScript","Kotlin","angular","Python"]
plt.xticks(x, x_text)
#barh es para posicionar desde y, bar es desde x
plt.bar(x,y,color="green")
plt.ylabel('Numeros')
#Se guarda en la carpeta principal
plt.savefig('pruebaBarras.png')

#Mas informacion sobre bar https://pythonbros.com/grafica-de-barras-con-matplotlib/