# Importación de librerías
import numpy as np

#Configuración de parámetros Gamma y Alpha del algoritmo
gamma = 0.75 # Factor de descuento
alpha = 0.9  # Ratio de aprendizaje

#######################################
####    Definimos el entorno      #####
#######################################

# Definición de los estados
ubicacion_a_estado={'A':0,
                   'B':1,
                   'C':2,
                   'D':3,
                   'E':4,
                   'F':5,
                   'G':6,
                   'H':7,
                   'I':8,
                   'J':9,
                   'K':10,
                   'L':11}
# definicion acciones
acciones = [0,1,2,3,4,5,6,7,8,9,10,11]

# definicion recompensas
            #  A,B,C,D,E,F,G,H,I,J,K,L  accion/estado(ubicación)
r = np.array([[0,1,0,0,0,0,0,0,0,0,0,0], # A
              [1,0,1,0,0,1,0,0,0,0,0,0], # B
              [0,1,0,0,0,0,1,0,0,0,0,0], # C
              [0,0,0,0,0,0,0,1,0,0,0,0], # D
              [0,0,0,0,0,0,0,0,1,0,0,0], # E
              [0,1,0,0,0,0,0,0,0,1,0,0], # F
              [0,0,1,0,0,0,1000,1,0,0,0,0], # G
              [0,0,0,1,0,0,1,0,0,0,0,1], # H
              [0,0,0,0,1,0,0,0,0,1,0,0], # I
              [0,0,0,0,0,1,0,0,1,0,1,0], # J
              [0,0,0,0,0,0,0,0,0,1,0,1], # K
              [0,0,0,0,0,0,0,1,0,0,1,0]])# L

#######################################
# Contrucción de Q-Learning############
#######################################

#Inicialización de los valores Q
q = np.array(np.zeros([12,12]))#inicializamos la matriz de 12x12 como la de recompensa a 0

################################################
# Implementación del proceso de Q-Learning######
################################################
for i in range(0,1000):
    estado_actual=np.random.randint(0,12)
    acciones_seleccionadas=[]
    for j in range(12):
        if r[estado_actual,j]>0:
            acciones_seleccionadas.append(j)
    estado_siguiente=np.random.choice(acciones_seleccionadas)
    temporal_diference= r[estado_actual,estado_siguiente] + gamma*q[estado_siguiente,np.argmax(q[estado_siguiente,])] - q[estado_actual,estado_siguiente]
    q[estado_actual,estado_siguiente]+= alpha*temporal_diference

#############################################
#puesta en producción del algoritmo##########
#############################################    
#traducción inversa de estados(números) a ubicaciones (letras)
estados_a_ubicacion={state:ubicacion for ubicacion,state in ubicacion_a_estado.items()}

# creación de la función de la mejor ruta
def ruta(ubicacion_inicial, ubicacion_final):
    ruta=[ubicacion_inicial]
    siguiente_ubicacion = ubicacion_inicial
    while(siguiente_ubicacion!=ubicacion_final):
        estado_inicial=ubicacion_a_estado[ubicacion_inicial]
        estado_siguiente=np.argmax(q[estado_inicial,])
        siguiente_ubicacion=estados_a_ubicacion[estado_siguiente]
        ruta.append(siguiente_ubicacion)  
        ubicacion_inicial=siguiente_ubicacion
        
    return ruta

def mejor_ruta(ubicacion_inicial, ubicacion_intermedia, ubicacion_final):
    return ruta(ubicacion_inicial, ubicacion_intermedia) + ruta(ubicacion_intermedia, ubicacion_final)[1:]


print("Mejor ruta: ")
print(mejor_ruta('E', 'K','H'))
