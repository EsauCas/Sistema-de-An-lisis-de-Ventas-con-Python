import os
import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos
data = pd.read_csv('C:/Users/chane/Desktop/ProyectosCV/#1/ventas.csv')

# Producto más vendido
mas_vendido = data.groupby('Producto')['Cantidad'].sum()

# Gráfico de barras
mas_vendido.plot(kind='bar')
plt.title('Productos más vendidos')
plt.xlabel('Producto')
plt.ylabel('Cantidad')
plt.show()
