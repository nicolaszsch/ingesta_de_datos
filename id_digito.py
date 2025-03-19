import cv2
import numpy as np
from id_resolucion_imagen import ResolucionImagen
from id_funciones import gen_head, gen_df
import id_configuracion 

class Digito:
    """
    Cada Digito viene contenido en una imagen, de una resolución específica, 
    desde la cual se debe identificar. Cada objeto Digito almacena la
    información necesaria de los pixeles de la imagen que contiene al dígito,
    la transforma, y además la utiliza para la identificación de éste, a 
    través de un modelo de Regresión Logística, ya generado en la 
    ResolucionImagen.

    Atributos:
    res_imag (ResolucionImagen): Resolución de la imagen que contiene el
        dígito a identificar. 
    cod_ima (str): Código que identifica la imagen que contiene el dígito.
    pca_pixs (np.ndarray): Información reducida, a través de PCA, de los 
        pixeles de la imagen. Inicialmente 'None'.
    valor (int): Valor del dígito a identificar. Inicialmente 'None'.
    """


    def __init__(self, img_reso: ResolucionImagen, img_cod):  
        """
        Inicializa una instancia de la clase Digito. 

        Parámetros:
        img_reso (ResolucionImagen): Indica la resolución de la imagen que 
            contiene el dígito a identificar.
        img_cod (str): Indica el código que identifica la imagen que contiene
            al dígito.

        El atributo res_imag se inicializa con 'ima_reso', mientras que 
        cod_ima se inicializa con img_cod.
        """
        self._res_imag = img_reso
        self._cod_ima = img_cod
        self._pca_pixs = None   ### Será necesario guardar? Pix o pca_pix?
        self.__valor = None

    def asignar_pca_pixs(self):
        """
        Obtiene la información reducida de los pixeles de la imagen, a través
        de gen_pca_pixs, para luego asignarla al atributo pca_pixs.
        """
        pca_pix = self.__gen_pca_pixs()
        self._pca_pixs = pca_pix

    def asignar_valor(self): 
        """
        Identifica el valor del digito contenido en la imagen, a través de
        gen_valor, para luego asignarla al atributo valor.
        """
        # confirmar que pix es como debe ser
        val = self.__gen_valor()
        self.__valor = val 

    @property
    def valor(self):
        """ Método que retorna el atributo valor."""
        return self.__valor

    def __gen_pca_pixs(self):
        """
        Genera y retorna la información reducida de los pixeles de la imagen.
        
        Primero obtiene la informació de todos los pixeles con gen_pixs, 
        para luego trasnformarla en un DataFrame, y así poder utilizar el 
        modelo de PCA, ya generado en Resolucion Imagen, para poder reducir
        la dimensionalidad. Finalmente retorna la información reducida.

        Retorna:
        pca_trans (np.ndarray): Información reducida, a través de PCA, de los
            pixeles de la imagen.
        """
        pca = self._res_imag.mod_pca 
        pix = self.__gen_pixs()
        header = gen_head(self._res_imag.n_pix, 'ID', 'Pix')  # Revisar si no se puede sacar directamente de la info del csv
        df_pix = gen_df(np.array(pix).reshape(1,-1), header, 'ID')     
        pca_trans = pca.transform(df_pix)
        return pca_trans

    def __gen_valor(self):
        """
        Determina el valor del dígito, a partir de la información de la imagen.

        Identifica el valor del dígito, utilizando el modelo de Regresión 
        Logística, ya generado, sobre la información reducida de los pixeles,
        calculada previamente. Finalmente retorna el valor.

        Retorna:
        predic (int): Predicción, por parte del modelo, del valor del digito
            contenido en la imagen, en base a la información de ésta. 
        """
        # supongo que validar que pix es como debe ser y resImag pueda utilizarse
        log_reg = self._res_imag.reg_log       
        predic = log_reg.predict(self._pca_pixs.reshape(1,-1))
        return predic
    
    def __gen_pixs(self):
        """
        Genera y retorna información sobre los pixeles de la imagen.

        Primero genera el nombre del archivo de la imagen, para luego "leerla"
        con OpenCV, para luego separarla en las matrices de los 3 colores, con
        los cuales, mediante aplanar_y_normalizar, se genera una lista con los
        valores normalizados de cada pixel de la imagen. Finalmente retorna
        esta lista.

        Retorna:
        pix (list): Lista con los valores normalizados de cada pixel de la
            imagen. 
        """
        a = id_configuracion.ano
        m = id_configuracion.mes
        d = id_configuracion.dia
        nombre = (a + '-' + m + '-' + d + '_'+ self._cod_ima)
        imagen = cv2.imread(nombre + '.jpeg')
        B, G, R = cv2.split(imagen)
        pix = self._res_imag.aplanar_y_normalizar(nombre, B, G, R)
        return pix
