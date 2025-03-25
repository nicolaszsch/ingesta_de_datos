from interaccion_usuario import acciones_a_realizar
from interaccion_modulos_y_clases import (asingar_fecha, 
                                         obtencion_y_validacion_valores, 
                                         gen_registro)

def main():
    """
    Primero se llama a asignar_fecha, en que se le pide al usuario que
    indique la fecha de los Valores sobre los que hay que trabajar, 
    pues se la necesita, por ejemplo, para identificar los archivos de
    las imágenes que contienen los Digitos. 
    Luego se llama a obtencion_y_validacion_valores, a través de la 
    cual se calculan y obtienen los Valores, y se validan que estén 
    correctos.
    Después de esto se llama gen_registro, para generar el Registro que
    gestiona la historia de los Valores.
    Por último se llama a acciones_a_realizar, con la cual se comunica
    con el usuario, y así éste le indique qué se debe hacer con los 
    valores obtenidos.
    """      
    asingar_fecha()
    valores_act, validacion = obtencion_y_validacion_valores()
    registro_hist = gen_registro(valores_act)
    acciones_a_realizar(validacion, registro_hist)

if __name__ == "__main__":
    main()