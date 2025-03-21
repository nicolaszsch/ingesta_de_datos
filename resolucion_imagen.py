from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
import pandas as pd
from configuracion import porcent_info_pca
                                   
class ResolucionImagen:
    """
    Indica la dimensión, es decir la cantidad de pixeles, de las imágenes que 
    contiene el Digito a identificar. Dada que el modelo de identificación se
    realiza para una resolución específica, cada objeto ResolucionImagen es el
    que genera y almacena el modelo que identifica los dígitos contenidos en
    cada imagen.    
    En este caso, las resoluciones utilizadas son de 8x15 y 13x25 pixeles.

    Atributos:
    pix_x (int): Cantidad de pixeles de ancho de esta resolución.      
    pix_y (int): Cantidad de pixeles de alto de esta resolución.
    n_pix (int): Cantidad total de pixeles de esta resolución.
    df_train (pd.DataFrame): Información asociada a los pixeles de las
        imágenes usadas para entrenar el modelo de esta resolución.
    mod_pca (PCA): Modelo PCA para generar la disminución de componentes según
        la cantidad de información que se debe retener. Inicialmente 'None'.
    pca_train (pd.DataFrame): Información asociada a los pixeles de las 
        imágenes usadas para entrenar el modelo de esta resolución, posterior 
        a la reducción de componetes usando PCA. Inicialmente 'None'.
    reg_log (LogisticRegression): Modelo de Regresión Logística utilizado para 
        identificar los dígitos de cada imagen de esta resolución. 
        Inicialmente 'None'.
    """


    def __init__(self, px: int, py: int, train_data: pd.DataFrame,
                 hist: pd.DataFrame):
        """
        Inicializa una instancia de la clase ResolucionImagen. 
        
        Parámetros:
        px (int): Cantidad de pixeles de ancho de las imágenes de esta
            resolución.
        py (int): Cantidad de pixeles de alto de las imágenes de esta
            resolución.
        train_data (pd.DataFrame): Información asociada a los pixeles de las
            imágenes usadas para entrenar el modelo de esta resolución.
        hist (pd.DataFrame): Información histórica de valor de cada dígito de
            las imágenes utilizadas para entrenar el modelo.
        
        El atributo pix_x se inicializa con 'px', pix_y se inicializa con 'py',
        n_pix con el producto de ambos, mientras que df_train se inicializa
        con train_data.
        Finalmente se llama a inicializar_atributos_modelo para configurar el 
        modelo PCA y el modelo de Regresión Logística, determinando los 
        atributos que inicializan en None.
        """
        # Atributos de dimensiones
        self._pix_x = px       
        self._pix_y = py       
        self.__n_pix = px*py    
        
        # Atributos de modelo de identificación de dígitos
        self._df_train = train_data  
        self.__mod_pca = None  
        self._pca_train = None  
        self.__reg_log = None     
        
        # Método que inicializa los atributos asociados al modelo
        self.__inicializar_atributos_modelos(hist)

    def aplanar_y_normalizar(self, name, matB, matG, matR):
        """
        Conviérte las matrices de colores en una gran lista normalizada.
        
        Forma parte del proceso de generación de información asociada a los 
        valores de los pixeles de cada imagen. Transforma las matrices de 
        colores en un arreglo en que cada elemento representa al valor del
        pixel, llevado a escala de grises, normalizado.
        
        Parámetros:
        name (str): Nombre del archivo que contiene la imagen e identificador.
        matB-G-R (np.ndarray): Matrices, de cada color (azul-verde-rojo), con 
            los valores por cada pixel de la imagen.

        Retorna:
        pix (list): Lista con la valores normalizados, en escala de grises, de
            cada pixel de la imagen. El primer elemento es el ID de la imagen.
        """
        pix = [None] * (self.__n_pix + 1)        
        pix[0] = name
        for i in range(0, self._pix_y):
            for j in range(0, self._pix_x):
                pix[i*self._pix_x + j + 1] = (
                    0.2989 * matR[i][j] +
                    0.5870 * matG[i][j] +
                    0.1140 * matB[i][j]
                ) / 255 
        return pix

    @property
    def n_pix(self):
        """ Método que retorna el atributo n_pix."""
        return self.__n_pix

    @property
    def mod_pca(self):
        """ Método que retorna el atributo mod_pca."""
        return self.__mod_pca

    @property
    def reg_log(self):
        """ Método que retorna el atributo reg_log."""
        return self.__reg_log

    def __inicializa_mod_pca(self):
        """
        Establece el modelo de reducción de componentes.
        
        Determina el modelo PCA para la reducir la dimensionalidad, en base a
        la información de los pixeles de todas las imágenes de entrenamiento
        de la resolución.
        """
        #confirmar que dfTRain != none, u otro error // ver qu eel nombre de
        #la precisión está bien (al final de una de las conversaciones con el RA está la pregunta)        
        pca_mat = PCA(porcent_info_pca)
        pca_mat.fit(self._df_train)
        self.__mod_pca = pca_mat

    def __inicializa_reg_log(self, hist):
        """
        Establece el modelo para la identificación de imágenes.
        
        Genera el modelo de Regresión Logística para la identificación de los
        Digitos a partir de imágenes del set de entrenamiento de la resolucón.
        
        Parámetro:
        hist (pd.DataFrame): Información histórica de valor de cada dígito de
            las imágenes utilizadas para entrenar el modelo.    
        """
        #confirmar que pcaTRain (exista, creo) 
        log_r = LogisticRegression(solver = 'lbfgs')
        log_r.fit(self._pca_train, hist)
        self.__reg_log = log_r    
        
    def __inicializa_pca_train(self): 
        """
        Genera reducción de dimensionalidad de las imágenes de entrenamiento.
        
        Establece los datos de pixeles de las imágenes de entrenamiento de
        la resolución posterior a la reducción de dimensionalidad, utilizando 
        el modelo PCA previamente generado.
        """
        # confirmar que dfTRain y calcPCA != none
        self._pca_train = self.__mod_pca.transform(self._df_train)
        
    def __inicializar_atributos_modelos(self, hist): 
        """
        Inicializa los atributos asociados a la creación del modelo.
        
        Llama los distintos métodos que establecen cada atributo que conforman
        el modelo de identificación de dígitos.

        Parámetros:
        hist (pd.DataFrame): Información histórica de valor de cada dígito de
            las imágenes utilizadas para entrenar el modelo.
        """ 
        self.__inicializa_mod_pca()
        self.__inicializa_pca_train()
        self.__inicializa_reg_log(hist)