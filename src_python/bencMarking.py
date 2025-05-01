import random
import time
from metodos_Ordenamiento import MetodosOrdenamiento

class Benchmarkin:
    def __init__(self):
        print('Bench inicializado')

    def ejemplo(self):
        self.mOrdenamiento=MetodosOrdenamiento()
        
        arreglo=self.buildArreglo(1000)
        self.mOrdenamiento=MetodosOrdenamiento()

        tarea=lambda:self.mOrdenamiento.sortByBubble(arreglo)
        tiempoMillis= self.contar_con_current_time_milles(tarea)
        tiempoNano=self.contar_con_current_nano_time(tarea)

        print(f'Tiempo en milisegundos:{tiempoMillis}')
        print(f'Tiempo en milisegundos:{tiempoNano}')


    def buildArreglo(self,size):
        array=[]
        for i in range (size):
            numero=random.randint(0,99999)
            array.append(numero)
        return array

    #import time
    #ejecutar tarea tarea()

    #x=time.time()

    def contar_con_current_time_milles(self,tarea):
        x=time.time()
        tarea()
        fin=time.time()
        return  fin-x


    #x=time.time_ns()
    def contar_con_current_nano_time(self,tarea):
        x=time.time_ns()
        tarea()
        fin=time.time_ns()
        return  (fin-x)/1_000_000_000.0
    
    def medir_tiempo(self,tarea,array):
        inicio=time.perf_counter()
        tarea(array)
        fin=time.perf_counter()
        return fin-inicio
    
