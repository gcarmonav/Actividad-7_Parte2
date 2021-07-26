# Actividad-7_Parte2

**Decisiones bajo incertidumbre**

**Por: Giovanna Andrea Carmona Valencia - Hilber García López**

## El problema del vendedor viajero

### 1. Planteamiento del problema

Un vendedor debe hacer un recorrido por las siguientes ciudades de Colombia en su carro (no necesariamente en este orden):

- Palmira
- Pasto
- Tuluá
- Bogota
- Pereira
- Armenia
- Caldas
- Valledupar
- Montería
- Soledad
- Cartagena
- Barranquilla
- Medellín
- Bucaramanga
- Cúcuta

Se desea obtener el orden óptimo, teniendo en cuenta el costo de desplazamiento entre ciudades, el cual se encuentra compuesto por el valor de la hora del vendedor, el costo de los peajes y el costo del combustible.

#### 1.1. Supuestos
**1.1.1. Valor de la hora del vendedor:**

Para este ejercicio se planteará un vendedor con un salario fijo equivalente a dos (2) salarios mensuales mínimos equivalentes a $1.817.052 más un salario variable promedio de $3.000.000 por concepto de comisiones, a estos valores se les agregaran los costos laborales a cargo del empleador como los aportes a seguridad social y parafiscales y los gastos por las prestaciones sociales, cuyos porcentajes  y valores se enuncian a continuación:

![imagen](https://user-images.githubusercontent.com/72627454/126932952-530bd3e1-5b05-4ac3-93c2-3ae81c1f63f7.png)

Los anteriores costos nos generan el gasto laboral total del vendedor:

![imagen](https://user-images.githubusercontent.com/72627454/126933836-35410971-8cd9-4fd0-8e65-9875457ca476.png)

Tomamos el costo total del empleado y lo dividimos por las horas mensuales laboradas en Colombia (240 horas/mes) y nos da un costo de $ 27.874 por hora, el cual será tomado en los algortimos de optimización.

**1.1.2. Vehículo utilizado:**

Dado que para este tipo de trabajos es necesario un carro que no consuma mucho combustible y que sea de gama media, se utilizará un vehículo Chevrolet Spark GT con un cilindraje de 1.200 y 80 HP que tiene un rendimiento promedio de 67 km/galón (tomado de https://www.autofact.com.co/blog/comprar-carro/mercado/carros-menor-consumo)

![imagen](https://user-images.githubusercontent.com/72627454/126933668-2a095150-5041-487f-97ad-ea08bb96439e.png)

**1.1.3. Costo de gasolina y velocidad promedio:**

Para el cálculo del costo de combustible se tomó como referencia un costo de $ 8.525 por galón (tomado de https://es.globalpetrolprices.com/Colombia/gasoline_prices/)

Asimismo, para efectos de cálcular la duración de los viajes de acuerdo a las distancias entre las ciudades se trabajó con una velocidad promedio de 70km/hora.

**1.1.4. Peajes y distancias:**

Las distancias entre ciudades fueron tomadas de google.maps mientras que los costos de peajes

### 2. Resultados


### 3. Referencias

https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35

http://www.jcreview.com/fulltext/197-1578037726.pdf?1578371869

https://towardsdatascience.com/using-ant-colony-and-genetic-evolution-to-optimize-ride-sharing-trip-duration-56194215923f
