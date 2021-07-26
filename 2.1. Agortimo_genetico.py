"""
0=Bogotá, 1=Palmira, 2=Medellín, 3=Pasto, 4=Tuluá, 5=Pereira, 6=Armenia, 7=Caldas, 8=Valledupar, 
9=Monteria, 10=Soledad, 11=Cartagena, 12=Barranquilla, 13=Bucaramanga, 14=Cúcuta

"""
import numpy as np, random
import matplotlib.pyplot as plt

## SE CREA LA MATRIZ DE DISTANCIA ENTRE CIUDADES
m_ciudades=np.empty([15,15])
m_ciudades[0,:]=[0, 448, 415.6, 723, 369.7, 320, 280.9, 432, 864.6, 756.3, 995.7, 1038.6, 1001.5, 397.7, 555.8]
m_ciudades[1,:]=[448, 0, 407.7, 400.4, 78, 194.4, 164.9, 383.8, 1105.3, 806.8, 1095.8, 1033.4, 1242.1, 749.3, 942]
m_ciudades[2,:]=[415.6, 407.7, 0, 792.6, 325, 224, 268, 23.3, 748, 404, 696, 631, 706, 392, 584]
m_ciudades[3,:]=[723, 400.4, 792.6, 0, 469, 586, 556, 775, 1496, 1198, 1629, 1424, 1633, 1140, 133]
m_ciudades[4,:]=[369.7, 78, 325, 469, 0, 117, 87.8, 307, 1028, 730, 1022, 956, 1165, 672, 864]
m_ciudades[5,:]=[320, 194.4, 224, 586, 117, 0, 44.6, 191, 913, 614, 1045, 841, 1049, 557, 748]
m_ciudades[6,:]=[280.9, 164.9, 268, 556, 87.8, 44.6, 0, 236, 940, 659, 1073, 885, 1077, 584, 775]
m_ciudades[7,:]=[432, 383.8, 23.3, 775, 307, 191, 236, 0, 769, 425, 717, 651, 727, 413, 604]
m_ciudades[8,:]=[864.6, 1105.3, 748, 1496, 1028, 913, 940, 769, 0, 433, 298, 362, 301, 448, 539]
m_ciudades[9,:]=[756.3, 806.8, 404, 1198, 730, 614, 659, 425, 433, 0, 343, 246, 354, 613, 704]
m_ciudades[10,:]=[995.7, 1095.8, 696, 1629, 1022, 1045, 1073, 717, 298, 343, 0, 129, 12, 580, 670]
m_ciudades[11,:]=[1038.6, 1033.4, 631, 1424, 956, 841, 885, 651, 362, 246, 129, 0, 119, 622, 712]
m_ciudades[12,:]=[1001.5, 1242.1, 706, 1633, 1165, 1049, 584, 727, 301, 354, 12, 622, 0, 586, 676]
m_ciudades[13,:]=[397.7, 749.3, 392, 1140, 672, 557, 584, 413, 448, 613, 580, 622, 586, 0, 199]
m_ciudades[14,:]=[555.8, 942, 584, 133, 864, 748, 775, 604, 539, 704, 670, 712, 676, 199, 0 ]

## SE CREA LA MATRIZ DE PEAJES ENTRE CIUDADES
m_peajes=np.empty([15,15])
m_peajes[0,:]=[0, 99500, 68100, 128000, 99500, 66200, 51700, 40500, 96500, 80500, 132000, 122300, 134200, 41200, 39700]
m_peajes[1,:]=[99500, 0, 90000, 37500, 26300, 49600, 47900, 72700, 147000, 156500, 184700, 186000, 184700, 122000, 137100]
m_peajes[2,:]=[68100, 90000, 0, 118400, 90000, 40400, 54900, 28300, 83300, 79600, 105500, 96000, 105500, 58300, 73400]
m_peajes[3,:]=[128000, 37500, 118400, 0, 37500, 78000, 76300, 101100, 175400, 184900, 213100, 214400, 213100, 150400, 165500]
m_peajes[4,:]=[99500, 26300, 90000, 37500, 0, 49600, 47900, 72700, 147000, 156500, 184700, 186000, 184700, 122000, 137100]
m_peajes[5,:]=[66200, 49600, 40400, 78000, 49600, 0, 14500, 23100, 97400, 106900, 135100, 136400, 135100, 72400, 87500]
m_peajes[6,:]=[51700, 47900, 54900, 76300, 47900, 14500, 0, 37600, 94300, 121400, 132000, 150900, 132000, 69300, 84400]
m_peajes[7,:]=[40500, 72700, 28300, 101100, 72700, 23100, 37600, 0, 74300, 94800, 112000, 124300, 112000, 49300, 64400]
m_peajes[8,:]=[96500, 147000, 83300, 175400, 147000, 97400, 94300, 74300, 0, 45900, 47600, 35700, 47600, 47000, 28200]
m_peajes[9,:]=[80500, 156500, 79600, 184900, 156500, 106900, 121400, 94800, 45900, 0, 44100, 51700, 44100, 8300, 64200]
m_peajes[10,:]=[134200, 184700, 105500, 213100, 184700, 135100, 132000, 112000, 47600, 44100, 0, 34500, 6000, 84700, 65900]
m_peajes[11,:]=[122300, 186000, 96000, 214400, 186000, 136400, 150900, 124300, 35700, 51700, 34500, 0, 34500, 72800, 54000]
m_peajes[12,:]=[134200, 184700, 105500, 213100, 184700, 135100, 132000, 112000, 47600, 44100, 6000, 34500, 0, 84700, 65900]
m_peajes[13,:]=[41200, 122000, 58300, 150400, 122000, 72400, 69300, 49300, 47000, 8300, 84700, 72800, 84700, 0, 15100]
m_peajes[14,:]=[39700, 137100, 73400, 165500, 137100, 87500, 84400, 64400, 28200, 64200, 65900, 54000, 65900, 15100, 0 ]

#SE ESTABLECEN LOS PARÁMETROS INICIALES
a_ciudades=np.array(list(range(0,15))) #Lista de las ciudades a trabajar
poblacion=30 #Número de individuos de nuestra población
num_padres=poblacion #Cantidad de padres
mutacion_r=0.1 #Índice de mutación
num_gen=1000 #Número de generaciones
vh_v=27874 #Valor por hora del vendedor
v_c=8525 #Valor del galon de gasolina
pop=np.array([random.sample(list(a_ciudades), len(a_ciudades)) for _ in range(poblacion)])
## LA FUNCIÓN P_RUTA SE ENCARGA DE GENERAR UNA RUTA Y CREAR UNAS VARIABLES QUE GUARDEN LAS DISTANCIAS Y VALOR DE PEAJES DE DICHA RUTA
def P_ruta (a_ciudades, m_ciudades,m_peajes): # A la función le ingresan las dos matrices de valores
    ##Se inicializan las variables
    ruta_f=list(range(0,16)) #Ruta final
    ruta=list(a_ciudades) #Se convierte la ruta actual a una lista (entra en forma de array)
    ruta_d=np.empty([1,15]) #Distancias de la ruta
    ruta_p=np.empty([1,15]) #Peajes de la ruta
    
    ##En este for se indexa los valores de distancia y peajes que hay entre ciudad y ciudad de la ruta
    ##Para ellos se utilizan dos variable "c y c_sig" que guardan la ciudad actual y la siguiente
    ## Para así poder colocar dichas posiciones en las matrices de distancias y peajes que hay desde una ciudad a la otra
    for j in range(0,(len(ruta)-1)):
        c=ruta[j]
        c_sig=ruta[j+1]
        ruta_d[0,j]=m_ciudades[c,c_sig]
        ruta_p[0,j]=m_peajes[c,c_sig]
    ##Este if se utiliza ya que en realidad son 16 ciudades incluyendo que el recorrido debe 
    ## terminar donde inició. Sin embargo en la primera iteración las rutas creadas no tienen
    ## esta posición '16' -->
    if len(ruta)>15:
        ruta_f=ruta

    else:
        ## --> Así que se agrega solo si la ruta de entrada tiene unicamente 15 ciudades
        ## De lo contrario la ruta final queda igual
        ruta_f[0:15]=ruta
        ruta_f[15]=ruta[0] ##Se indexan las primeras 15 posiciones con la ruta de ingreso
                           ## Y despues en la posición final se coloca la primera ciudad
        ruta_d[0,j+1]=m_ciudades[c_sig,ruta[0]]
        ruta_p[0,j+1]=m_peajes[c_sig,ruta[0]] ##Se busca tanto la distancia como el valor de peajes
                                              ## que hay entre la última ciudad y la primera
    return ruta_f,ruta_d,ruta_p


## LA FUNCIÓN RUTAS SE ENCARGA DE REALIZAR EL CÁLCULO DEL COSTE DE CADA RUTA
def Rutas (m_ciudades, poblacion,a_ciudades,m_peajes,vh_v,v_c):
    ##Se inicializan las variables con sus respectivos tamaños
    pop_rutasd=np.empty([poblacion,15]) #Matriz que muestra la distancia de cada indviduo (ruta)
    pop_rutas=np.empty([poblacion,16],int) #Matriz de la población con las 16 ciudades
    pop_rutasp=np.empty([poblacion,15]) #Matriz que muestra el valor de los peajes de cada indviduo (ruta)
    mtriz_coste=np.empty([poblacion,3]) #Matriz que almacena los tres parametros que conforman el coste
                                        # costo peajes + costo horas + costo combustible
    ##Se utiliza un for para realizar el proceso de cálculo del coste de cada ruta
    for i in range(poblacion):
        #Se utiliza la función P_ruta
        pop_rutas[i,:],pop_rutasd[i,:],pop_rutasp[i,:]=P_ruta(a_ciudades[i,:],m_ciudades,m_peajes)
        d=pop_rutasd[i,:]
        p=pop_rutasp[i,:]
        mtriz_coste[i,0]=(sum(d)/67)*v_c #Se realiza el cálculo de la distancia final de la ruta
                        ## y se haya el valor del combustible necesario para recorrer dicha distancia
                        
        mtriz_coste[i,1]=sum(p) #Se realiza el cálculo del costo total en peajes de la ruta
        
        mtriz_coste[i,2]=(sum(d)/70)*vh_v #Se realiza el cálculo de la distancia final de la ruta
                        ## y se haya el valor de las horas necesarias para recorrer dicha distancia y así el valor total de hora del vendedor
    return pop_rutas, mtriz_coste

##La función "Función_padres" se encarga de organizar la población de mayor a menor 
# desempeño respecto a la función de coste
def Funcion_padres(ruta_p,mtriz_coste, num_padres):
    ## Seinicializan las variables
    padres_f = np.empty((num_padres,ruta_p.shape[1]),int) #matriz de población final
    fitness=np.empty([mtriz_coste.shape[0],1]) #matriz del coste total de cada ruta
    for i in range(mtriz_coste.shape[0]):
        fitness[i]=sum(mtriz_coste[i,:]) #Se calcula el coste total de cada ruta
    best_fitness=sorted(fitness) #Se ordena de mayor a menor desempeño
    for i in range(num_padres):
        x=np.where(fitness==best_fitness[i])
        padres_f[i,:]=ruta_p[x[0],:] #Se organiza la población de mayor a menosr desempeño
    return padres_f,best_fitness

## LA FUNCIÓN DE CROSSOVAR SE ENCARGA DE CRUZAR LOS PADRES TOMANDO TRES VALORES FIJOS DEL
## PRIMER PADRE Y COLOCANDO DICHOS VALORES EN LA MISMA POSICIÓN QUE SE ENCUENTRAN PERO EN EL PADRE DOS
def crossover (padres,poblacion):
    ## Se inicializan las variables
    padres=padres[:,0:15] #con el fin de evitar errores se suprime el recorrido de la última ciudad a la primera
    des=np.array([random.sample(list(a_ciudades), len(a_ciudades)) for _ in range(poblacion)])
    des_f=np.array([random.sample(list(range(0,17)), 16) for _ in range(poblacion)])
    ubs=np.empty([1,4],int)
    for i in range(poblacion-1):
        p1=random.sample(list(padres[i,:]), 3) #Se escogen los valores del primer padre a utilizar
        p2=list(padres[i+1,:]) #Se escoge el segundo padre
        for j in range(len(p1)):
            #Se indexa en las posiciones del primer padre sus valores en el segundo padre 
            ub=np.where(int(p1[j])==padres[i,:])
            ubs[0,j]=ub[0]
            t=p2.index(p1[j])
            p2[t],p2[int(ubs[0,j])]=p2[int(ubs[0,j])],p2[t]
        des[i,:]=p2
    des_f[:,0:15]=des
    des_f[:,15]=des[:,0]# Ya hecho el cruce se vuelve a color el recorrida de la última ciudad a la primera
                    ## para que se tenga en cuenta al momento de calcular el coste de la ruta
    return des_f

##LA FUNCION DE MUTACION SE ENCARGA DE CAMBIAR UNA CIUDAD DE POSICIÓN DE FORMA ALEATORIA
## TENIENDO EN CUENTA EL ÍNDICE DE MUTACIÓN QUE PERMITIRÁ DECIDIR CUÁL SERÁ LA CIUDAD CAMBIADA
def mutacion(des, mutacion_r):
    des_f=np.array([random.sample(list(range(0,17)), 16) for _ in range(poblacion)])
    #Para esta mutación también se quital el recorrido de la última ciudad a la primera, ya que ésta también puede cambiar y generaría un error
    des=des[:,0:15]
    for i in range(des.shape[0]):
        for swapped in range(des.shape[1]):
            if(random.random() < mutacion_r): ## Este if es el que se encarga de que se cambie la ciudad
                                            ## solo si el número generado aleatoriamente es menor al
                                            ## índice de mutación
                swapWith = int(random.random() * des.shape[1])
                city1 = des[swapped,swapped]
                city2 = des[swapped,swapWith]
                des[swapped,swapped] = city2
                des[swapped,swapWith] = city1 ## Se cambia la posición de la ciudad elegida
    des_f[:,0:15]=des
    des_f[:,15]=des[:,0] ## Se vuelve a colocar la distancia entre la última ciudad a la primera
    return des

for generacion in range(num_gen): ## Se utiliza el for para realizar el proceso de cración de las generaciones
    ruta_p,ruta_d=Rutas(m_ciudades,poblacion,pop,m_peajes,vh_v,v_c) #Se calcula primero el coste de la población inicial
    padres,fitness=Funcion_padres(ruta_p,ruta_d, num_padres) #Después se organiza de mayor a menor desempeño
    cr=crossover (padres,poblacion) #Se realiza el cruce
    pop=mutacion(cr, mutacion_r) #Se realiza la mutación de la población

##DESPUÉS DE LA CREACIÓN DE TODAS LAS GENERACIONES, SE VUELVE A CALCULAR EL COSTE Y 
## ORGANIZAR DE MAYOR A MENOR DESEMPEÑO
ruta_p,ruta_d=Rutas(m_ciudades,poblacion,pop,m_peajes,vh_v,v_c)
poblacion_f,fitness=Funcion_padres(ruta_p,ruta_d, num_padres)
print("Mejor Ruta: ", poblacion_f[0, :])
print("Valor de Coste (COP) menor: ", fitness[0])

##SE GRAFICA EL CAMBIO DEL VALOR DE COSTE RESPECTO A LAS ITERACIONES
plt.plot(sorted(fitness, reverse=True))
plt.xlabel("# Iteraciones")
plt.ylabel("Función de Coste")
plt.title('Variación Función de Coste con {} iteraciones'.format(num_gen))
plt.show()




        