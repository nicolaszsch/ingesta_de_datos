# Ingesta de Datos

Este proyecto en verdad es la sección de EL (extracción y carga) de un proyecto más grande (que espero subir pronto).

El propósito de éste es la obtención de información de unos indicadores en la Web que se actualizan diariamente. 
Esto se realiza a través de la obtención de imágenes de los valores obtenidos de la Web, la idendtificación de los valores contenidos en las imágenes, y la actualización del registro histórico de los valores.
En estricto rigor, en el proyecto subido a este repositorio no hay extracción ni carga, ya que falta el paso de la obtención de imágenes (las capturas se realiza con el programa Auto Screen Capture, y la automatización de las capturas se realiza con AutoHotkey) y el de la carga (se actualiza el archivo que leerá el programa dónde se analizará la información).
Lamentablemente no existe una API de la Web para extraer de forma más directa la información, pero es posible encontrar finalmente una forma más simple para la obtención de los datos, pero aún así este proyecto al menos logra el reconocimiento e imágenes en dígitos, que ya en sí es una base para realizar otra cosas. 

Se intenó que el código fuera lo más simple y directo posible, está documentado y siguiendo las convenciones de PEP8, más allá de pueden encontrarse algún error al respecto.
Si se encuentra una mejor forma de hacer algo, o derechamente una corrección, agradecería mucho hacérmela llegar.  

Instalación


Mejoras por realizar