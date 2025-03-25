"""
Este módulo contiene las funciones con las que el main se relaciona con
otros módulos o clases. En este caso hay una función para conectarse
con el módulo de configuración para actualizar variables de fecha, 
además de otra función que se utiliza para la relación con la clase
Valores, generando que cada uno de los Montos pueda calcularse de forma
correcta, mientras que la última es para generar el registro que 
gestionará la historia. 
"""

from valores import Valores
from registro import Registro
from interaccion_usuario import solicitar_fecha
import configuracion

def asingar_fecha():
    """
    Obtiene la información de la fecha y así asignarla a las variables.
    
    Primero obtiene el mes y día de las imágenes a trabajar, a través
    de consultarle al usuario, para luego fijarla en las variables 
    globales ubicadas en el módulo de configuración.    
    """ 
    m , d = solicitar_fecha()
    configuracion.mes = m
    configuracion.dia = d

def obtencion_y_validacion_valores():
    """
    Se insta el objeto Valores, generando que se insten en cadena las
    instancias de Montos, Digitos y ResolucionImagen respectivas.
    Luego, a través de asignar_valores_montos, que produce que cada
    Monto de Valores calcule su valor, a partir de la identificación de
    los Digitos que los componen, desde sus imágenes respectivas.
    Finalmente llama a validacion para verificar si hubi errores en la
    identificación de los Digitos, a través de la relación que debiese
    existir entre los Valores. Finalmente retorna el resultado de esta
    validación.

    Retorna:
    validar (bool): True si resultaron correctas las validaciones,
        False si hubo al menos 1 que no.
    """
    set_valores = Valores()
    set_valores.asignar_valores_montos()
    validar = set_valores.validacion()
    return set_valores, validar

def gen_registro(values):
    """
    Insta una instancia de la clase Registro, que gestiona la historia
    de los Montos "nucleares". Para esto llama gen_montos_con_historia
    que retorna los Montos que tienen Registro, los que se necesiran
    para instar Registro.

    Parámetro:
    values (Valores): Objeto Valores, a partir del cual se pueden
        obtener los Montos que deben tener Registro ("nucleares").
    
    Retorna:
    registro_hist (Registro): Objeto Registro, que permite gestionar la
        historia de los Montos "nucleares". 
    """ 
    registro_hist = Registro(values.gen_montos_con_historia())
    return registro_hist