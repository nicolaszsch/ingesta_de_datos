# Ingesta de Datos

Este proyecto, en estricto rigor, es la sección de TL (transformación y carga) de un proyecto más grande, el que espero subir pronto.

El propósito es la obtención de los valores de unos indicadores que hay en la Web, que se actualizan diariamente. 
Esto se realiza a través de la obtención de imágenes de los indicadores, la posterior idendtificación de los valores contenidos en las imágenes, reconociendo cada uno de los dígitos, y la actualización del registro histórico de los valores. El proyecto subido al este repositorio no considera la obtención de las imágenes, éstas se agregan directamente a éste, pero mi idea sería, si es posible, subir esa sección en algún momento, al menos explicando cómo hacerlo.  
Lamentablemente no existe una API de la Web para extraer de forma más directa la información, pero es posible que, más adelante, se pueda encontrar una forma más simple para la obtención de los datos, pero aún así este proyecto al menos logra el reconocimiento de dígitos contenidos en imágenes, que ya en sí es una base para realizar otra cosas. 
Para el reconocimiento de los dígitos contenidos en las imágenes, se realiza, por ahora, un modelo de identificación de dígitos por cada una de las resoluciones de las imágenes que contienen los dígitos de los indicadores. En este caso se utiliza la resolución de 8x15 y 13x25 pixeles. Para la identificación de las imágenes se utiliza Machine Learning, es específico Regresión Logística sobre la información, de la cual se hace reducción de dimensionalidad con PCA, de los pixeles de éstas.

Se intenó que el código fuera lo más simple y directo posible, está documentado y siguiendo las convenciones de PEP8, más allá de pueden encontrarse algún error al respecto.
Si se encuentra una mejor forma de hacer algo, o derechamente una corrección, agradecería mucho hacérmela llegar, al igual que cualquier otra duda o solicitud al respecto.

### Instalación y uso

##### 1. Clonar el repositorio:

Abrir terminal y ejecutar el siguiente comando:

git clone https://github.com/nicolaszsch/Ingesta.git

##### 2. Crear y activar entorno virtual: (Opcional)

Si se desea trabajar con un entorno virtual, se debe crear éste ejecutando:

py -m venv venv

Y después se debe activar:

.\venv\Scripts\Activate   (Windosws)

##### 3. Instalar librerías utilizadas:

Para instalar las librerías en el entorno virtual, ejecutar:

pip install -r requirements.txt

##### 4. Ejecución del código

Para ejecutar el programa, se debe ejecutar el main, es decir, 'main.py'.

Se debe tener en cuenta que el registro histórico de los valores se encuentra en 'Valores.csv', que en está versión sólo tiene información utilizada como set de entrenamiento, es decir los primeros 7 registros asociados a cada indicador (hasta 2025-01-07).
Al ejecutar, se le solicitará la fecha de las imágenes sore la cual se identificarán los valores. Por ahora sólo se pedirá mes y día, los cuales deben ir en formato MM y DD (ejemplo: 01, 12, 17, 31)
Se puede verificar las fechas disponibles identificando la fecha de las imágenes en el fichero (en este momento el 01-08). Estaré constantemente subiendo las imágenes más actuales.
Algunos de los valores están relacionados con otros, por lo que estas relaciones se utilizan para validar que los valores identificados se hayan determinado bien.
Si la validación es correcta, se le dará la posibilidad de actualizar el registro de los indicadires. Si se elige no, se le dará la posibilidad de imprimir el registro incluyendo los nuevos valores. Si se elige sí, se le preguntará si se actualiza en el archivo con los registros, por lo que si decide que sí, se actualizará el archivo que contiene la historia con los valores identificados por el modelo, y si se elige no, se creará el archivo "Valores Nuevos. csv", donde se cargará el registro de los indicadores (este último archivo no generará actualización de la historia utilizada por el modelo). 


### Mejoras por realizar al proyecto

*Generar validaciones a errores potenciales
*Adecuar flujo de acciones al interactuar con el usuario [^1]
*Qué la generación de los pixeles sea directamente en escala de grises y liberar al código de esa transformación
*Fusionar los modelos de identificación de dígitos de cada resolución en uno que comprenda el de ambas resoluciones utilizadas
*Agregar en proyecto el entrenamiento del modelo

[^1]: Este proyecto no tenía la intención de compartirse en su inicio, por lo que hay varias cosas que faltan por adecuar para que no sólo sirva para el propósito que tengo yo, si no otras funcionalidades que tengan sentido. Esto se ejemplifica muy bien con el flujo de las posibles acciones que entrega el proyecto.
