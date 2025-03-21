"""
Este módulo contiene las funciones con las que el programa se relaciona con el
usuario, que, básicamente, es para saber cobn qué fecha trabajar, y qué hacer
con los Valores obtenidos. 
"""

def solicitar_fecha():
    """
    Solicita al usuario el año, mes y día de la fecha de la que que se 
    requiere obtener los Valores. El print() es para que el mensaje se vea
    más ordenado. 

    Retorna:
    m, d (str): Mes y día de la fecha de cada imagen, utilizados para
        que los Digitos puedan identificar sus valores, y así los Montos 
        puedan calcular el suyo.
    """
    print()
    m = input('Mes: MM \n') # Mes  # Se deben hacer la validciones de que la fecha corresponda a las que hay disponibles.
    d = input('Día: DD \n') # Día
    return m, d


def acciones_a_realizar(valid, reg_hist): # Dejar a, m, d como variable
    """
    Se le da opciones al usuario respecto de qué hacer con los datos obtenidos.

    Si la validación de datos falla en alguna relación, se muestra un mensaje
    de que las validaciones no son correctas, por lo que no se actualizan los
    valores. Si las validaciones se cumplen, se le da opciones al usuario. La 
   primera es sobre si actualizar el archivo con los nuevos valores, si la
   respuesta es:
        - Sí, Se pregunta si actualizar el archivo de prueba o no, por lo que,
            si la respuesta es sí, se actualizará un archivo de prueba (que no
            es el del que extrae la información Registro), si la respuesta es
            no, se actualizará el archivo que contiene la información extraída
            por Registro. Cualquier otra respuesta no actualiza el archivo.
            Cada opción es complementada con su mensaje correspondiente.
        - No, Se pregunta si imprimir la tabla con los valores actualizados,
            si la respuesta es sí se imprimiran los valores, cualquier otra
            respuesta finalizará el programa.
        - Cualquier otra respuesta genera el mensaje de que no se responde por
            un sí o un no, por lo que no se actualizará el archivo.
    Para cada respuesta de sí o no, se aceptan las distintas opciones en 
    minúcula, o la primerla letra mayúscula, y la opción con tilde.
    """ #Podría haber una forma de aceptar moníscular o mayúsculas
    if valid:
        actualizar = input('Dada que las validaciones están correctas,'
                           ' ¿actualizar el archivo con los nuevos valores?:'
                           ' / Sí o no \n')
        if actualizar == 'No' or actualizar == 'no':
            print('No se actualiza el archivo con los nuevos valores')
            imprimir = input('¿Imprimir al menos la tabla como hubiese quedado'
                             ' actualizada? / Sí o no \n')
            if (imprimir == 'Sí' or imprimir == 'Si' or imprimir == 'sí' or 
                imprimir == 'si'):
                reg_hist.agregar_a_historia()
                reg_hist.imprimir_historia()
        elif (actualizar == 'Sí' or actualizar == 'Si' or actualizar == 'sí' 
              or actualizar == 'si'):
            reg_hist.agregar_a_historia()
            exportar = input('¿Actualizar en el archivo de prueba? / Sí o no'
                             '\n')
            if (exportar == 'Sí' or exportar == 'Si' or exportar == 'sí' or
                exportar == 'si'): 
                reg_hist.exportar_historia('Valores Nuevos.csv')
                print('Se actualiza el archivo de prueba')
            elif exportar == 'No' or exportar == 'no':
                reg_hist.exportar_historia('Valores.csv')
                print('Se actualiza el archivo con los nuevos valores')
            else:
                print('No se respondió un sí o un no, por lo que NO se '
                      'actualizan los valores')
        else:
            print('No se respondió un sí o un no, por lo que NO se actualizan '
                  'los valores')
    else:
        print('Dada que las validaciones no se cumplieron, no se actualiza el '
              'archivo con los nuevos valores')