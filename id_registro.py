import pandas as pd
import numpy as np
from id_monto import Monto
from id_funciones import gen_df, leer_csv
import id_configuracion

class Registro:
    """
    Gestiona y maneja la historia de los Valores.

    Puede agregar información, la de los Valores, a la historia, además de
    tener la capacidad de imprimirla, o exportarla a un archivo CSV que se
    indique. Al actualizarla al archivo de origen la historia queda disponible
    para las próximas lecturas.

    Atributos de Clase:
    dir_registros (str): Tiene la ubicación del archivo que contiene la
        historia ya registrada de los Montos "nucleares".

    Atributos de Instancia:
    historia (pd.DataFrame): Datos con la historia de los registros. 
        Inicialmente 'None'.
    montos (list[Monto]): Lista con los Montos "nucleares" que son los que
        cuentan con historia. 
    """


    def __init__(self, record_amounts: list[Monto]):
        """
        Inicializa una instancia de la clase Registro. 
        
        Parámetros:
        record_amounts (pd.DataFrame): Lista con los Montos "nucleares" que 
        son los que cuentan con historia.
        
        El atributo montos se inicializa record_amounts. Finalmente se llama a
        inicializa_historia para generar la historia de los Montos
        correspondientes.
        """
        self.__historia = None
        self._montos = record_amounts
        self.__inicializa_historia()

    def agregar_a_historia(self):
        """
        Agrega al Registro los Valores actuales.

        Primero se genera la lista que se utiliza para el encabezado, para
        luego generar la lista con los Montos a registrar. Luego llama a 
        gen_df para convertir la lista en un DataFrame (genrando de forma 
        transitoria un arreglo de NumPy), y así poder concatenarla a la
        la historia registrada actualmente, formando la historia actualizada,
        que es la que se le asigna al atributo historia.
        
        XXXXXXXXXXXXXXXXX
        Parámetros:
        a, m, d (str): Año, mes y día de la fecha de los Montos que se
        añadirán, que se utilizan para formar el índice de estos nuevos Montos. 
        """
        a = id_configuracion.ano
        m = id_configuracion.mes
        d = id_configuracion.dia
        head = ['Fecha', 'AFP A', 'AFP E', 'APV A', 'APV A15', 'APV E',
                'APV E15']
        nuevos_valores = [d + "-" + m + "-" + a[2] + a[3],
                          int(self._montos[0].valor_monto),
                          int(self._montos[1].valor_monto),
                          int(self._montos[2].valor_monto),
                          int(self._montos[3].valor_monto),
                          int(self._montos[4].valor_monto),
                          int(self._montos[5].valor_monto)]
        df_nuevos_valores = gen_df(
                    np.array(nuevos_valores, dtype = object).reshape(1,-1),
                    head, 'Fecha')
        registro_actualizado = pd.concat([self.__historia, df_nuevos_valores])
        self.__historia = registro_actualizado


    def exportar_historia(self, nombre_archivo):
        """
        Exporta la historia a un archivo CSV con el nombre indicado.
        Si el nombre del archivo es el de origen, se actualizará la historia
        de entrada al modelo.

        Parámetro:
        nombre_archivo (str): Nombre del archivo CSV al que se exportará la
            historia.
        """
        self.__historia.to_csv(nombre_archivo)
     
    def imprimir_historia(self):
        """ Imprime la historia."""
        print(self.__historia)

    def __inicializa_historia(self):
        """
        Determina la historia, a partir de lo registrado hasta el momento.

        Primero obtiene la información del archivo de origen, en la ubicación
        dir_registros, para luego asiasignársela al atributo historia.
        """
        ### CSV
        reg_hist = leer_csv(id_configuracion.dir_registros)
        self.__historia =  reg_hist
    
    # def eliminar(self):

    