#!/usr/bin/python
# Codeado por Elvis Gamboa Machado / @Gamboamej @Pythonologo en IG

# En Python tiene varios tipos de datos compuestos estándar disponibles por defecto en el interprete, 
# como los tipos numéricos, secuencias, mapeos y conjuntos usados para agrupar otros valores.

# Para el caso de las estructuras de datos se usan variables y constantes las cuales usan operadores para tratar los tipos de datos estándar.
# Clasificación

#Los tipos de datos compuestos estándar se pueden clasificar como los dos siguientes:

#    Mutable: su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.
#    Inmutable: su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución.

#Se pueden resumir los tipos de datos compuestos estándar en la siguiente tabla:

# Números inmutables 	
#    int 	    entero
#    float 	    coma flotante
#    complex 	complejo
#    bool 	    booleano

# Secuencias inmutables 	
#    str 	    cadena de caracteres
#    unicode 	cadena de caracteres Unicode
#    tuple 	    tupla
#    xrange 	rango inmutable

# Secuencias mutables 	
#    list 	    lista
#    range 	    rango mutable

#Mapeos 	
#    dict 	    diccionario
#Conjuntos mutables 	
#set 	conjunto mutable
#Conjuntos inmutables 	
# frozenset 	conjunto inmutable

#Otros tipos de datos incorporados, se describen a continuación:

#Objeto integrado 	NoneType 	        objeto None.
#Objeto integrado 	NotImplementedType 	objeto NotImplemented.
#Objeto integrado 	ellipsis 	        objeto Ellipsis.
#Objeto integrado 	file 	            objeto file.

# Lista la teoria! Codigo a la obra...

#    esto es un  int       entero
manzanas = 10
#    esto es un  int 	   entero 
numero_hormigas = 456966786151987643
#    esto es un  float 	coma flotante
precio_total = 1.5908576
#    esto es un  complex 	complejo
complejo = 2.1 + 7.8j
#    esto es un  bool 	    booleano



# podemos comprobarlo con la función type
print ("La variable 'manzanas' tiene un valor de", manzanas, "y es de tipo:", type(manzanas), "\n")
print ("La variable 'numero_hormigas' tiene un valor de", numero_hormigas, "y es de tipo:", type(numero_hormigas), "\n")
print ("La variable 'precio_total' tiene un valor de", precio_total, "y es de tipo:", type(precio_total), "\n")
print ("La variable 'complejo' tiene un valor de", complejo, "y es de tipo:", type(complejo), "\n")
