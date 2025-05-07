import matplotlib
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]
nombre_linea="lInea 1"
plt.plot(x,y,label=nombre_linea,color="blue")

#agregar para metro

plt.title("primer grafico")
plt.xlabel("datos eje x")
plt.ylabel("datos eje y")
plt.legend()
plt.show()