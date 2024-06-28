******************************************************************************
****  Caso práctico de optimización de flujos en un almacén de e-commerce ****
******************************************************************************

Solución de IA desarrollada mediante algoritmo de Q-Learning

El enfoque de la solución planteada está basada en la optimización de un almacén que contiene distribuidos los productos a lo largo de 12 zonas distintas. Según los clientes van haciendo los pedidos, un robot con IA trata de recoger los productos y llevarlos al lugar indicado por la ruta mas optima, partiendo de la base de que el robot cada vez podría estar en una ubicación. El objetivo del algoritmo debe ser que siempre tome la ruta más corta a la ubicación indicada, sea cual sea la ubicación desde la que comienza(qlearning.py), y tener la opción de ir a través de  ubicación intermedia al objetivo final(qlearning_v2.py).

El almacén tendrá la siguiente configuración:

<img width="1000" alt="Captura de pantalla 2024-06-28 a las 23 02 51" src="https://github.com/agarpu/Optimizacion-de-Procesos/assets/174133000/5c9cb683-9ce8-4b24-ae4e-46c7cd60ac54">

Para el desarrollo nos hemos basado en la ecuación de Bellman, que junto con la transformación de Markov y el uso de diferencias temporales nos ha permitido darle al robot el conocimiento suficiente para que aprenda que ruta debe usar en cada momento.
