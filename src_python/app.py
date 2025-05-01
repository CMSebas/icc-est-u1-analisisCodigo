import bencMarking as Ben
from metodos_Ordenamiento import MetodosOrdenamiento


#ejecutar benchmark
if __name__ == "__main__":
    print("Funciona")
    benchmark= Ben.Benchmarkin()
    metodos=MetodosOrdenamiento()

    tam=100
    arreglo_base=benchmark.buildArreglo(tam)


    metodos={
        "burbuja":metodos.sortByBubble,
        "seleccion":metodos.sort_seleccion
    }

    resultados=[]
    for nombre,metodo in metodos.items():
        tiempo=benchmark.medir_tiempo(metodo,arreglo_base)
        tuplaResultado=(tam,nombre,tiempo)
        resultados.append(tuplaResultado)
    
    for resultado in resultados:
        tam,nombre,tiempo=resultado
        print(f"Tamaño:{tam},Metodo:{nombre},Tiempo{tiempo:.6f}segundos")

    