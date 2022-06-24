#!/usr/bin/python
# Codeado por Elvis Gamboa Machado / @Gamboamej @Pythonologo en IG

#Variables: 
# Es un nombre que se refiere a un objeto que reside en la memoria. 
# El objeto puede ser de alguno de los tipos vistos (número o cadena de texto), o alguno de los otros tipos existentes en Python.

#Cada variable debe tener un nombre único llamado identificador. 
# Es muy de ayuda pensar las variables como contenedores que contienen data la cual puede ser cambiada después a través de técnicas de programación.
# En Python existe una convencion que recomiendas.

#Reglas y convención de nombres

#Algunas reglas y convenciones de nombres para las variables y constantes:

    #Nunca use símbolos especiales como !, @, #, $, %, etc.

    #El primer carácter no puede ser un número o dígito.

    #Las constantes son colocadas dentro de módulos Python y significa que no puede ser cambiado.

    #Los nombres de constante y variable debería tener la combinación de letras en 
    # minúsculas (de a a la z) o 
    # MAYÚSCULAS (de la A a la Z) o 
    # dígitos (del 0 al 9) o un underscore (_). Por ejemplo:

        #    snake_case
        #    MACRO_CASE
        #    camelCase
        #    CapWords

    #Los nombres que comienzan con guión bajo (simple _ o doble __) se reservan para variables con significado especial

    #No pueden usarse como identificadores, las palabras reservadas.


# Ejemplo de nombre de varibles: nombre_usuario, nu_puestos, in_activo.
# Ejemplo de nombre de constantes: USER_DB_SERVER, PORT_DB_SERVER, DB_NAME.

# Lista la teoria! Codigo a la obra...

# esto es una variable de tipo      str cadena de caracteres
nombre_usuario = "gamboamej"
# esto es una variable de tipo      int entero
nu_puestos = 10
# esto es una constante de tipo     int entero 
PORT_DB_SERVER = 4321

# Imprimimos el Resultado
print ("La variable 'nombre_usuario' tiene un valor de", nombre_usuario, "y es de tipo:", type(nombre_usuario), "\n")
print ("La variable 'nu_puestos' tiene un valor de", nu_puestos, "y es de tipo:", type(nu_puestos), "\n")
print ("La constante 'PORT_DB_SERVER' tiene un valor de", PORT_DB_SERVER, "y es de tipo:", type(PORT_DB_SERVER), "\n")