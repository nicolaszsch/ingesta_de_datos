"""
Este módulo contiene las funciones con las que el programa se relaciona
con el usuario, que, básicamente, es para saber con qué fecha trabajar,
y qué hacer con los Valores obtenidos. 
"""

from configuracion import dir_registros, dir_nuevo

def solicitar_fecha():
    """
    Solicita al usuario el año, mes y día de la fecha de la que que se 
    requiere obtener los Valores. El "print()" es para que el mensaje
    se vea más ordenado.

    Retorna:
    m, d (str): Mes y día de la fecha de cada imagen, utilizados para
        que los Digitos puedan identificar sus valores, y así los 
        Montos puedan calcular el suyo.
    """
    print()
    m = input('Mes: MM \n')
    d = input('Día: DD \n')
    return m, d


def acciones_a_realizar(valid, reg_hist):
    """
    Se da opciones al usuario sobre qué hacer con los datos obtenidos.

    Si la validación de datos falla en alguna relación, se muestra un
    mensaje de que las validaciones no son correctas, por lo que no se
    actualizan los valores. Si las validaciones se cumplen, se le da 
    opciones al usuario. La primera es sobre si actualizar el archivo
    con los nuevos valores, si la respuesta es:
        - Sí, se pregunta si actualizar el archivo con los registros o
            no, por lo que, si la respuesta es sí, se actualizará ese
            archivo, mientras que, si la respuesta es no se actualizará
            un archivo de prueba (que no es el del cual Registro extrae
            la información). Cualquier otra respuesta no actualiza el
            archivo. Cada opción es complementada con su mensaje 
            correspondiente.
        - No, se pregunta si imprimir la tabla con los valores 
            actualizados, si la respuesta es sí se imprimiran los 
            valores, cualquier otra respuesta finalizará el programa.
        - Cualquier otra respuesta genera el mensaje de que no se 
            responde por un sí o un no, por lo que no se actualizará el
            archivo.
    Para cada respuesta de sí o no, se aceptan distintas opciones, en 
    minúscula, o la primerla letra mayúscula y la opción con tilde.
    """ 
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
            exportar = input('¿Actualizar en el archivo con los registros? /'
                             'Sí o no\n')
            if (exportar == 'Sí' or exportar == 'Si' or exportar == 'sí' or
                exportar == 'si'): 
                reg_hist.exportar_historia(dir_registros)
                print('Se actualiza el archivo con los nuevos valores')
            elif exportar == 'No' or exportar == 'no':
                reg_hist.exportar_historia(dir_nuevo)
                print('Se genera el archivo de prueba con el registro')
            else:
                print('No se respondió un sí o un no, por lo que NO se '
                      'actualizan los valores')
        else:
            print('No se respondió un sí o un no, por lo que NO se actualizan '
                  'los valores')
    else:
        print('Dada que las validaciones no se cumplieron, no se actualiza el '
              'archivo con los nuevos valores')