from id_digito import Digito
from id_resolucion_imagen import ResolucionImagen
        
class Monto:
    """
    Los Montos se compone de Digitos, que según su orden establecen el valor 
    de éste. Cada Digito contenido en una imagen contiene un identificador 
    compuesto por una letra y un número, la primera indica el Monto al que
    pertenece (identificador del Monto), mientras que el número indica la
    posición del dígito en el Monto. Todo los Digitos de un Monto tienen la
    misma resolución. Cada objeto Monto es el que llama a los métodos de sus
    Digitos para identificarlos, y con esto poder calcular el valor 
    correspondiente al Monto, teniendo en cuenta su orden interno.  

    Atributos:
    largo (int): Cantidad de Digitos que componen el Monto.
    cod_monto (str): Código (letra) que identifica al Monto.    
    digitos (list[Digito]): Lista de los Digitos que componen el Monto, la
        cual inicializa vacía.
    valor_monto (int): Valor del Monto, calculado a partir de los valores de
        los Digitos que lo componen. Inicialmente 'None'.
    """

    def __init__(self, imgs_reso: ResolucionImagen, amou_len: int, 
                 amou_cod: str):
        """
        Inicializa una instancia de la clase Monto. 

        Parámetros:
        imgs_reso (ResolucionImagen): Resolución de las imágenes que contienen
            los Digitos que componen el Monto.
        amou_len (int): Indica la cantidad de Digitos que componen el Monto.
        amou_cod (str): Indica el código que identifica al Monto.

        El atributo largo se inicializa con 'amou_len', mientras que cod_monto
        con se inicializa con 'amou_cod'.
        Finalmente se llama a inicializa_digitos para generar todos los 
        Digitos que componen el monto, indicandole su resolución.
        """
        # Atributos con las características y elementos del Monto
        self._largo = amou_len  ### Probablemente sacar
        self._cod_monto = amou_cod ### Probablemente sacar
        self._digitos = []
        self.__valor_monto = None

        # Método para inicializar los Digitos del Monto
        self.__inicializa_digitos(imgs_reso)

    #Modificado
    def asignar_valor_monto(self):
        """
        Obtiene el valor del Monto, para asignarlo al atributo valor_monto.
        
        Primero llama al método identificar_valores, que llama métodos de sus
        Digitos para que estos identifiquen sus valores, para luego poder 
        utilizar gen_valor_monto, que en base a los valores ya identificados 
        de los Digitos, y al orden de estos, calcula el valor del monto, y así
        lo asigna al atributo valor_monto.
        """
        self.__identificar_valores() #que las fechas estén en el formato correcto
        val = self.__gen_valor_monto()
        self.__valor_monto = val

    @property
    def valor_monto(self):
        """ Método que retorna el atributo valor_monto"""
        return self.__valor_monto

    def __identificar_valores(self):
        """
        Genera la identificación de los valores de cada Digito.

        Primero llama al método asignar_pca_pixs, que calcula la información
        reducida de los pixeles de la imagen, para luego poder llamar a 
        asignar_valor que permite a cada Digito identificar su valor. 
        """
        for i in range(self._largo): ### Largo como len(digitos)
            self._digitos[i].asignar_pca_pixs()
            self._digitos[i].asignar_valor()

    def __gen_valor_monto(self):
        """
        Genera y retorna el valor del Monto en base al de sus Digito.

        Multiplica el valor de cada Digito por la potencia de 10 
        correspondiente a su posición en el Monto, para sumarlos y así obtener
        el valor. Finalmente retorna el valor.

        Retorna:
        num (int): Valor calculado del Monto.
        """
        #Validación digitos con valor
        num = 0
        for i in range(self._largo):  ### Largo como len(digitos)
            num += self._digitos[i].valor * 10**i
        return num


    def __inicializa_digitos(self, img_reso):
        """
        Determina la lista digitos, agregandole cada Digito correspondiente.

        Genera el código de cada imagen, cod_imag, como un str compuesto por
        el código del Monto (la letra correspondiente) además de la posición
        del digito que contiene. A partir de esto y de la resolución de la
        imagen que corresponda, añade a la lista los Digitos que va instando,
        con lo que queda completa la lista digitos.

        Parámetro:
        img_reso (ResolucionImagen): Resolución de las imágenes que contienen
            cada dígito que compone el monto.
        """
        for i in range(self._largo): ### Recibir largo como parámetro
            cod_imag = self._cod_monto + str(i+1) ### Recibir cod_monto como parámetro
            self._digitos.append(Digito(img_reso, cod_imag))
