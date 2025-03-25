from monto import Monto
from resolucion_imagen import ResolucionImagen
from funciones import leer_csv
from configuracion import (PIX_X,PIX_Y, dir_data, dir_hist,
                           CODS_MONTOS, LAR_MONTOS, IDS_13X25, IDS_REGISTRO)

class Valores:
    """
    Los Valores se componen de Montos. Es en Valores que se llama a los
    métodos de cada Monto para que calculen su valor, mediante la 
    identificación del valor de sus Digitos, contenidos en las imágenes,
    para luego realizar una validación para verificar que no hubiese 
    ningún problema o error en alguna de las identificaciones de los
    valores de cada Digito. Para esto se debe tener en cuenta que 
    algunos de los Montos tienen registro, que son los Montos 
    "nucleares", es decir que no se desprenden de otros, mientras que
    los Montos "no nucleares" son los que sí se desprenden de otros 2
    (no es necesario tener registro de Montos que se pueden deducir a
    partir de otros). La razón de identificar el valor de los Montos
    "no nucleares" es justamente ocuparlos como validadores, para 
    verificar que se cumpla la relación que tiene que existir entre 
    cada uno de estos Montos con los 2 de los cuales se desprende.

    Atributos:
    resoluciones (list[ResolucionImagen]): Lista con cada 
        ResolucionImagen usada en el proyecto, la cual inicializa vacía.
    montos (list[Monto]): Lista con los Montos que componen Valores, la
        cual inicializa vacía.
    """


    def __init__(self):
        """
        Inicializa una instancia de la clase Monto. 

        Se llama a inicializa_resoluciones para generar cada
        ResolucionImagen utilizadas en el modelo, es decir la de 8x15 y
        13x25 pixeles, y se llama a innicializa_montos, para generar 
        cada Monto que compone los Valores.
        """
        self._resoluciones = []
        self.__montos = [] 
        self.__inicializa_resoluciones()
        self.__inicializa_montos()

    def asignar_valores_montos(self):
        """
        Genera que cada Monto obtenga y almacene su valor, llamando 
        asignar_valor_monto para cada uno.
        """            
        for i in range(len(CODS_MONTOS)): 
            self.__montos[i].asignar_valor_monto()

    def validacion(self):
        """
        Valida que se cumpla la relación que debe haber en los Montos.
        Retorna el resultado de la validación.

        Usando el método validar, que confirma si el tercer valor que
        se le entrega es resultado de la suma de los 2 anteriores, se
        va validando si se cumplen todas las relaciones que deben
        eixstir. Si alguna falla, se muestra un mensage indicando error,
        e identificando cual de las relaciones es la que falla. Si se 
        cumplen todas, se confirma que todas están correctas. Se 
        retorna el resultado de la validación.
        Las relaciones que se deben verificar son:
        Monto C + Monto J = Monto D
        Monto A + Monto B = Monto C
        Monto E + Monto K = Monto J
        Monto F + Monto H = Monto K
        Monto G + Monto I = Monto E

        Retorna:
        validador (bool): True si se cumplen todas las validaciones, 
            False si falla al menos una de ellas.
        """
        validador = self.__validar(self.__montos[6].valor_monto,
                                   self.__montos[8].valor_monto,
                                   self.__montos[4].valor_monto)
        if validador:
            validador = self.__validar(self.__montos[5].valor_monto,
                                       self.__montos[7].valor_monto,
                                       self.__montos[10].valor_monto)
            if validador:
                validador = self.__validar(self.__montos[4].valor_monto,
                                           self.__montos[10].valor_monto,
                                           self.__montos[9].valor_monto)
                if validador:
                    validador = self.__validar(self.__montos[0].valor_monto,
                                               self.__montos[1].valor_monto,
                                               self.__montos[2].valor_monto)
                    if validador:
                        validador = self.__validar(
                                                self.__montos[2].valor_monto,
                                                self.__montos[9].valor_monto,
                                                self.__montos[3].valor_monto)
                        if validador:
                            print('Están correctas todas las validaciones')
                        else:
                            print('Lectura Incorrecta. Falla la validación del'
                                  'Monto D') 
                    else:
                        print('Lectura Incorrecta. Falla la validación del'
                              'Monto C') 
                else:
                    print('Lectura Incorrecta. Falla la validación del Monto'
                          ' J')
            else:
                print('Lectura Incorrecta. Falla la validación del Monto K')
        else:
            print('Lectura Incorrecta. Falla la validación del Monto E') 
        return validador

          
    def imprimir_montos(self):
        """Imprime cada Monto contenido en Valores"""
        for i in range(len(CODS_MONTOS)):

                print(self.__montos[i].valor_monto)

    def gen_montos_con_historia(self):
        """
        Genera y retorna lista con los Montos que deben tener registro.

        Para esto se basa en la información contenida en la lista
        IDS_REGISTRO, que indica, através de los índices, los Montos 
        que cuentan con registro histórico, los cuales se agregan a una
        lista, que finalmente se retorna.

        Retrona:
        mont_hist (list[Monto]): Lista de los Montos que cuentan con
            registro histórico.
        """
        mont_hist = []
        for i in range(len(IDS_REGISTRO)):
            mont_hist.append(self.__montos[IDS_REGISTRO[i]])
        return mont_hist

    def __inicializa_resoluciones(self):
        """
        Genera la lista resoluciones, agregando cada ResolucionImagen.

        Para cada ResolucionImagen utilizada, llama a agregar_res_imags,
        que va a buscar la información del set de entrenamiento de ésta,
        y con esta información más la de su cantidad de pixeles,insta
        la ResolucionImagen correspondiente que agrega a lista. 
        """
        for i in range(len(dir_data)):
            self.__agregar_res_imags(PIX_X[i], PIX_Y[i], dir_data[i], 
                                     dir_hist[i]) 

    def __inicializa_montos(self):
        """
        Genera la lista montos, agregándole cada Monto correspondiente.

        Añade a la lista los Montos que va instando, indicándole a cada
        uno la ResolucionImagen, el largo y su código correspondiente.
        El largo y el código se obtienen de LAR_MONTOS y COD_MONTOS 
        respectivamente, que almacenan esta información para cada Monto,
        y respecto a la ResolucionImagen, la lista IDS_13x25 indica, a
        través de los índices, los Montos que tienen sus Digitos en 
        imágenes de una ResolucionImagen de 13x25 pixeles, mientras que
        el resto las tendrá en una de 8x15 pixeles, ambas ya 
        almacenadas en la lista resoluciones. 
        """      
        for i in range(len(CODS_MONTOS)):
            if i in IDS_13X25:
                self.__montos.append(Monto(self._resoluciones[1], 
                                           LAR_MONTOS[i], CODS_MONTOS[i]))
            else:
                self.__montos.append(Monto(self._resoluciones[0],
                                           LAR_MONTOS[i], CODS_MONTOS[i]))

    def __agregar_res_imags(self, x_pix, y_pix, data_dir, hist_dir): 
        """
        Agrega una ResolucionImagen a resoluciones, según parámetros.

        Dado que ResolucionImagen es la clase que genera y almacena el
        modelo que identifica el valor de los Digitos contenidos en las
        imágenes, se le otorga la información necesaria esta tarea, es
        decir, la relacionada con el set de entrenamiento del modelo de
        cada ResolucionImagen. Para esto busca la información, ya 
        generada, del set de entrenamiento respectivo en los archivos 
        que contienen los datos sobre los pixeles de las imágenes 
        (data_dir) y la clasificación en sus dígitos respectivos
        (hist_dir). Con esta información, más la de la cantidad de
        pixeles respectiva, se insta cada ResolucionImagen que se 
        agrega a la lista resoluciones.

        Parámetros:
        x_pix (int): Cantidad de pixeles de ancho de esta resolución.   
        y_pix (int): Cantidad de pixeles de alto de esta resolución.
        data_dir (str): Nombre del archivo que tiene la información de
            pixeles de las imágenes del set de entrenamiento.
        hist_dir (str): Nombre del archivo que tiene la información de
            la clasificacoón de las imágenes del set de entrenamiento.
         """
        train_data = leer_csv(data_dir)
        train_hist = leer_csv(hist_dir)
        self._resoluciones.append(ResolucionImagen(x_pix, y_pix, train_data,
                                                   train_hist))

    @staticmethod
    def __validar(a, b, c):
        """
        Valida si un valor (c) es la suma de otros dos (a y b). Retorna
        el booleano correspondiente.

        Parámetros:
        a, b, c (int): Valores a comparar.

        Retorna:
        bool: True si a + b == c, False en caso contrario.
        """
        return a + b == c