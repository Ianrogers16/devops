## hobbie
- se creo un programa donde te dice tus hobbies y se agrego una lista para guardar los dato y se agrego para que se intente agregar un numero
no deje subirlo 

## clase 3 
# if
- se implemento condicionales tales como 
- if  que lo que hace es que pasaria si tal condicicion se cumple o no 
- y el else que si no pasa la condicion  te arroja el resultado  

## clase docker 
# archivo main
Análisis de Ventas Automotrices con Pandas 🚗📊
la actividad  consiste en una aplicación de procesamiento de datos escrita en Python que utiliza la librería Pandas para calcular comisiones y generar estadísticas de rendimiento de ventas. El proyecto está completamente "containerizado" usando Docker para asegurar que se pueda ejecutar en cualquier entorno sin conflictos de dependencias.

Dockerfile: Configuración para construir la imagen del contenedor.


# Funcionalidades del Script
- El código realiza las siguientes operaciones de ingeniería de datos:Carga de Datos: Crea un DataFrame con registros de ventas (Vendedor, Modelo, Precio y Comisión).Cálculo de Comisiones: Genera una nueva columna calculando el monto exacto en moneda ($$Precio \times Comision$$).Agregación (Aggregation): 
- Utiliza el método .groupby() y .agg() para resumir el desempeño:Conteo de coches vendidos.Suma total de ingresos.Promedio de valor de venta.Total de comisiones acumuladas.Métricas de Negocio: Calcula el "Ticket Promedio" y ordena a los vendedores por volumen de ingresos.
# debug 
- se hace un debug del main lo cual lo ejecuta revisa los archivos
- despues de esto esto se ejecuta y se muestra la funcion del codigo 
- por ultimo se agrega el breakpoint en la parte de stats de los vendedores lo que hace que solo muestre las listas de ventas individuales  
