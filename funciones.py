"""
Módulo con funciones genéricas usadas en distintas partes del proyecto.
"""


import pandas as pd

def gen_head(n, ind, prefix):
    """
    Genera una lista con strings de los enteros entre 1 y n, con la 
    posibilidad de añadir un texto antes de cada número (prefix),
    pensados para que fueran el encabezado de cada campo en una tabla.
    Finalmente se retorna la lista con el encabezado.

    Parámetros:
    ind (str): Se utiliza para ser el encabezado del índice.
    prefix (str): Se utiliza como prefijo a los números para formar el 
        encabezado. Si prefix es un string vacío los encabezados sólo
        serán los enteros.

    Retorna:
    head (list[str]): Lista con elementos que se enumeran, para 
        utilizar de encabezado.
    """
    head = [None] * (n + 1)
    head[0] = ind
    for i in range(1, n + 1):
        head[i] = prefix + str(i)  
    return head


def gen_df(val, head, ind):
    """
    Genera un DataFrame a partir de una arreglo con datos.
    
    Parámetros:
    val (np.ndarray): Es la tabla que contiene los datos que se deben
        transformar en un DataFrame.
    head (list[str]): Lista que contiene los nombres de los campos que
        se utilizarán como encabezado.
    ind (str): Nombre del campo que será asignado como índice.

    Retorna:
    df (pd.DataFrame): DataFrame generado a partir de la información
        contenida en val.
    """
    df = pd.DataFrame(val, columns = head)
    df.set_index(ind, inplace = True)
    return df


def leer_csv(data_dir):
    """
    Lee y retorna la información contenida en el CSV que se encuentra 
    en data_dir.

    Parámetros:
    data_dir (str): Dirección con la ubicación del archivo CSV del cual
        se quiere obtener la información.

    Retorna:
    data (pd.DataFrame): Datos con la información contenida en el
        archivo CSV.
    """
    data = pd.read_csv(data_dir, header=0, parse_dates=False, index_col=0,
                       sep=',')
    return data