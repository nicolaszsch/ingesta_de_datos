from resolucion_imagen import ResolucionImagen
from digito import Digito
        
class Monto:
    """
    Cada Monto se compone de Digitos, que según su orden establecen el
    valor de éste. Cada Digito contenido en una imagen contiene un
    identificador compuesto por una letra y un número, la primera 
    indica el Monto al que pertenece (identificador del Monto),
    mientras que el número indica la posición del dígito en el Monto.
    Todo los Digitos de un Monto tienen la misma ResolucionImagen. Cada
    objeto Monto es el que llama a los métodos de sus Digitos para
    identificar sus valores, y con esto poder calcular el valor que le
    corresponde al Monto, teniendo en cuenta su orden interno.  

    Atributos:
    largo (int): Cantidad de Digitos que componen el Monto.
    cod_monto (str): Código (letra) que identifica al Monto.    
    digitos (list[Digito]): Lista de los Digitos que componen el Monto,
        la cual inicializa vacía.
    valor_monto (int): Valor del Monto, calculado a partir de los 
        valores de cada Digito que lo componen. Inicialmente 'None'.
    """
    def __init__(self, imgs_reso: ResolucionImagen, amou_len: int, 
                 amou_cod: str):
        """
        Inicializa una instancia de la clase Monto. 

        Parámetros:
        imgs_reso (ResolucionImagen): Indica la ResolucionImagen de las
            imágenes que contienen los Digitos que componen el Monto.
        amou_len (int): Indica la cantidad de Digitos que componen el 
            Monto.
        amou_cod (str): Indica el código que identifica al Monto.

        El atributo largo se inicializa con 'amou_len', mientras que
        cod_monto con se inicializa con 'amou_cod'.
        Finalmente se llama a inicializa_digitos para generar todos los 
        Digitos que componen el monto, indicandoles su ResolucionImagen.
        """
        # Atributos con las características y elementos del Monto
        self._largo = amou_len
        self._cod_monto = amou_cod
        self._digitos = []
        self.__valor_monto = None

        # Método para inicializar los Digitos del Monto
        self.__inicializa_digitos(imgs_reso)

    def asignar_valor_monto(self):
        """
        Obtiene el valor del Monto, asignándolo al atributo valor_monto.
        
        Primero llama al método identificar_valores, que llama a
        métodos de sus Digitos para que estos identifiquen sus valores,
        y así poder utilizar gen_valor_monto, que en base a los valores
        ya identificados de los Digitos, y al orden de estos, calcula
        el valor del Monto, y así lo asigna al atributo valor_monto.
        """
        self.__identificar_valores()
        val = self.__gen_valor_monto()
        self.__valor_monto = val

    @property
    def valor_monto(self):
        """ Método que retorna el atributo valor_monto"""
        return self.__valor_monto

    def __identificar_valores(self):
        """
        Genera la identificación de los valores de cada Digito.

        Primero, para cada Digito, llama al método asignar_pca_pixs,
        que calcula la información reducida de los pixeles de la imagen
        que lo contiene, para luego poder llamar a asignar_valor
        que genera que cada Digito identifique su valor. 
        """
        for i in range(self._largo):
            self._digitos[i].asignar_pca_pixs()
            self._digitos[i].asignar_valor()

    def __gen_valor_monto(self):
        """
        Genera y retorna el valor del Monto en base al de sus Digito.

        Para cada Digito, multiplica su valor por la potencia de 10 
        correspondiente a su posición en el Monto, para así sumar cada
        multiplicación y así obtener el valor del Monto. Finalmente 
        retorna el valor.

        Retorna:
        num (int): Valor calculado del Monto.
        """
        num = 0
        for i in range(self._largo): 
            num += self._digitos[i].valor * 10**i
        return num

    def __inicializa_digitos(self, img_reso):
        """
        Genera las lista digitos, agregandole cada uno de los Digitos.

        Para cada Digito, genera el código de cada imagen que lo 
        contiene, cod_imag, como un str compuesto por el código (letra)
        del Monto al que pertenece y la posición del Digito dentro del
        Monto. A partir de esto y de la ResolucionImagen 
        correspondiente, añade a la lista los Digitos que va instando,
        completando así la lista digitos.

        Parámetro:
        img_reso (ResolucionImagen): ResoluciónImagen de las imágenes
            que contienen cada Digito que componen el Monto.
        """
        for i in range(self._largo): 
            cod_imag = self._cod_monto + str(i+1) 
            self._digitos.append(Digito(img_reso, cod_imag))
