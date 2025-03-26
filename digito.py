import cv2
import numpy as np

from resolucion_imagen import ResolucionImagen
import configuracion 
from funciones import gen_head, gen_df

class Digito:
    """
    Cada Digito viene contenido en una imagen, de una ResolucionImagen
    específica, desde la cual se debe identificar. Cada objeto Digito
    almacena la información necesaria de los pixeles de la imagen que 
    lo contiene, la transforma, y además la utiliza para la
    identificación de éste, a través del modelo de Regresión Logística,
    ya generado en la ResolucionImagen correspondiente.

    Atributos:
    res_imag (ResolucionImagen): Resolución de la imagen que contiene 
        el Digito a identificar. 
    cod_ima (str): Código con el identificador de la imagen del Digito.
    pca_pixs (np.ndarray): Información, reducida a través de PCA, de 
        los pixeles de la imagen del Digito. Inicialmente 'None'.
    valor (int): Valor del dígito a identificar. Inicialmente 'None'.
    """
    def __init__(self, img_reso: ResolucionImagen, img_cod):  
        """
        Inicializa una instancia de la clase Digito. 

        Parámetros:
        img_reso (ResolucionImagen): Indica la ResolucionImagen de la
            imagen que contiene el Digito a identificar.
        img_cod (str): Indica el código que identifica la imagen que
            contiene al Digito.

        El atributo res_imag se inicializa con 'ima_reso', mientras que 
        cod_ima se inicializa con img_cod.
        """
        self._res_imag = img_reso
        self._cod_ima = img_cod
        self._pca_pixs = None  
        self.__valor = None

    def asignar_pca_pixs(self):
        """
        Obtiene la información reducida de los pixeles de la imagen que
        contiene al Digito, a través de gen_pca_pixs, para luego
        asignarla al atributo pca_pixs.
        """
        pca_pix = self.__gen_pca_pixs()
        self._pca_pixs = pca_pix

    def asignar_valor(self): 
        """
        Identifica el valor del Digito contenido en la imagen, a través
        de gen_valor, para luego asignarla al atributo valor.
        """
        val = self.__gen_valor()
        self.__valor = val 

    @property
    def valor(self):
        """ Método que retorna el atributo valor"""
        return self.__valor

    def __gen_pca_pixs(self):
        """
        Genera y retorna la información de los pixeles de la imagen.
        
        Primero obtiene la informació de todos los pixeles con gen_pixs, 
        para luego trasnformarla en un DataFrame, y así poder utilizar
        el modelo de PCA, ya generado en ResolucionImagen, para poder
        reducir la dimensionalidad. Finalmente retorna la información.

        Retorna:
        pca_trans (np.ndarray): Información reducida, a través de PCA,
            de los pixeles de la imagen que contiene al Digito.
        """
        pca = self._res_imag.mod_pca 
        pix = self.__gen_pixs()
        header = gen_head(self._res_imag.n_pix, 'ID', 'Pix')  
        df_pix = gen_df(np.array(pix).reshape(1,-1), header, 'ID')     
        pca_trans = pca.transform(df_pix)
        return pca_trans

    def __gen_valor(self):
        """
        Con la información de la imagen, determina el valor del Digito.

        Identifica el valor del Digito, utilizando el modelo de 
        Regresión Logística ya generado, sobre la información reducida
        de los pixeles de l aimagen, ya calculada previamente.
        Finalmente retorna el valor.

        Retorna:
        predic (int): Predicción, por parte del modelo, del valor del
            Digito contenido en la imagen. 
        """
        log_reg = self._res_imag.reg_log       
        predic = log_reg.predict(self._pca_pixs.reshape(1,-1))
        return predic
    
    def __gen_pixs(self):
        """
        Genera y retorna información sobre los pixeles de la imagen.

        Primero genera el nombre del archivo de la imagen que contiene
        al Digito (utilizado como identificador de la imagen), y a 
        partir de éste, genera la dirección de la ubicación del archivo,
        y así poder "leer" la imagen con OpenCV, para luego generar las
        matrices de los 3 colores, con las cuales, a través de 
        aplanar_y_normalizar, se genera una lista con los valores
        normalizados de cada pixel de la imagen. Finalmente retorna
        esta lista.

        Retorna:
        pix (list): Lista con los valores normalizados de cada pixel. 
        """
        a = configuracion.ano
        m = configuracion.mes
        d = configuracion.dia
        nombre = (a + '-' + m + '-' + d + '_'+ self._cod_ima)
        dir_img = ('Imagenes/'+ a + '-' + m + '-' + d + '/' + nombre)
        imagen = cv2.imread(dir_img + '.jpeg')
        B, G, R = cv2.split(imagen)
        pix = self._res_imag.aplanar_y_normalizar(nombre, B, G, R)
        return pix