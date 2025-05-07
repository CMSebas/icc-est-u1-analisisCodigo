import bencMarking as Ben
import matplotlib.pyplot as plt
from metodos_Ordenamiento import MetodosOrdenamiento
from datetime import datetime


#ejecutar benchmark
if __name__ == "__main__":
    print("Funciona")
    benchmark= Ben.Benchmarkin()
    metodos=MetodosOrdenamiento()

    tamanios=[500,1000,2000]
    resultados=[]
    

    for tam in tamanios:
        metodos_dict = {
            "burbuja": metodos.sortByBubble,
            "seleccion": metodos.sort_seleccion
        }

        arreglo_base = benchmark.buildArreglo(tam)

        for nombre, metodo in metodos_dict.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
            resultados.append((tam, nombre, tiempo))

    for tam, nombre, tiempo in resultados:
        print(f"Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")



        

    tiempos_by_metodo={
        "burbuja":[],
        "seleccion":[]
    }

    # Clasificar los métodos según su nombre
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

    fecha_actual = datetime.now()


    #Crear un grafica
    plt.figure(num=f"Sebastian Ceron:{fecha_actual}")



    for nombre,tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios,tiempos,label=nombre,marker="o")

    #agregar para metros
    
    plt.suptitle("Tiempo de metodos")
    plt.title(f"Sebastian Ceron:{fecha_actual}")
    plt.xlabel("tamaño del arreglo")
    plt.ylabel("tamaño en segundos")
    plt.grid(True)
    plt.legend()
    plt.show()
    