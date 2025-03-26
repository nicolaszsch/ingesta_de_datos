"""
Es es es el módulo de configuración. Contiene variables utilizadas en
el proyecto. Encontraremos los siguientes tipos de variables:
- Variables provenientes de interactuar con el usuario
- Variables utilizadas en ResolucionImagen
    -Características de la Resolución
    -Datos para el Modelo de Identificación de Imágenes
- Variables utilizadas en Registro
- Variables utilizadas en Valores
"""

# Variables provenientes de interactuar con el usuario
ano = '2025'
mes = None
dia = None
"""
Se le solicita al usuario información sobre la fecha, específicamente
del mes y día, dado que el año, por ahora, se asume como 2025, que es
necesaria para la obtención de los datos de los pixeles de las imágenes,
ya que el nombre del archivo de éstas contiene la fehca, lo que permite
identificar los valores de los Digitos, además de ser el dato utilizado
para identificar cada observación en Registro.
"""
 

# Variables utilizadas para Resolución de Imagen

# Características de la Resolución
PIX_X = [8, 13]
PIX_Y = [15, 25]

# Datos para el Modelo de Identificación de Imágenes
porcent_info_pca = 0.9
dir_data = ['pix_hist8x15.csv', 'pix_hist13x25.csv']
dir_hist = ['Hist8x15.csv', 'Hist13x25.csv']
"""
Información sobre los pixeles de cada resolución y también de datos
necesarios para la generación del módelo de identificación de imágenes,
como el porcentaje de información que se desea conservar al disminuir
la dimensionalidad con PCA, y los nombres de los archivos que contienen
la información del set de entrenamiento, respecto a la de los valores 
de sus pixeles y de la clasificación de sus dígitos.
"""


# Variables utilizadas en Registro

dir_registros = 'Valores.csv'
dir_nuevo = 'Valores Nuevos.csv'
"""
Nombre del archivo con contiene el Registro de la historia de los 
Valores que cuentan con éste, que se puede actualizar con los nuevos
valores que se obtienen de las imágenes. El segundo es el nombre del
archivo que se genera cuando no se quiere actualizar directamente el
archivo que contiene el Registro.
"""


# Variables utilizadas en Valores

CODS_MONTOS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
LAR_MONTOS = [8, 8, 8, 8, 6, 7, 6, 7, 6, 7, 7]
IDS_13X25 = [3, 9] # 'D', 'J'
IDS_REGISTRO = [0, 1, 5, 6, 7, 8] # 'A', 'B', 'F', 'G', 'H', 'I'
"""
Información sobre la definición de los Montos, como el código de cada
uno, su largo, su resolución (más específicamente, cuáles están 
contenidos en imágenes de 13x25 pixeles), y cuáles de ellos cuentan con
Registro.
"""