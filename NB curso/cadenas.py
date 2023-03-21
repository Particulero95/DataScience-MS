'''multilinea='Hechos acerca de la luna:\n No hay atmosfera.\n No hay sonido.' # al parecer \n nos da una pequeña sangria por default
# print(multilinea)
x
# Del mismo modo podemos dar salto de linea usando comillas triples 

multilinea2="""Hechos acerca de la luna: 
No hay atmosfera. 
No hay sonido."""
print(multilinea2)

#el comando .title() hace mayuscula la primera letra de cada palabra de una cadena 
print(multilinea.title())

prueba= "esta es una prueba"
prueba_2=prueba.title()

print(prueba_2)'''

#### Separar una cadena 

# Podemos usar el comando .split() para dividir una cadena y esto nos generara una lista
# Este comando toma por default a los espacios como separadores 

'''cadena= """Un día tiene: 24 hrs 
una hora tiene: 60 minutos 
un minuto tiene: 60 segundos"""
'''

'''lst=cadena.split()
print(lst)'''


#También podemos usar los saltos de linea como delimitadores para separar la cadena agregando el comando .split('\n') 
#Este comando funciona ya sea que demos saltos de linea usando \n o triples comillas dobles 
'''lst_1=cadena.split('\n')
print(lst_1)'''



### Búsqueda de un elemento dentro de una cadena 

#El comando 'in' buscara el argumento dentro de la cadena especificado y en caso de estar nos arrojara un True de lo contrario False

print("Moon" in "This text will describe facts and challenges with space travel") #Este argumento es Falso


print("Moon" in "This text will describe facts about the Moon") # Este argumento es cierto

#El comando .find() busca un argumento dentro de una cadana y nos regresa su posición dentro de la cadena 
