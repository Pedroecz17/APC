# Este programa tiene varios propositos, pero el proposito general es demostrar
# el uso de las funciones principales de python.

# EJERCICIO 1
suma = 2 + 5
resta = 4.4 - 4.3
mul = 6 * 3
div = 8.9 / 3

print('Ejercicio 1\nSuma:', suma, '\nResta:', resta, '\nMultiplicación:', mul, '\nDivisión:', div) # imprimir cada operación

#EJERCICIO 2
nombre = 'Pedro Esteban Carrión Zamora'
nombre_len = len(nombre.replace(' ', '')) # calcular la logitud del nombre, quitando espacios blancos

print('\nEjercicio 2\nNombre:', nombre, '\nLongitud:', nombre_len) # imprimir el nombee y su longitud

'''
Este programa calcula la logitud de una variable string llamada nombre y lo imprime el el interpretador
'''

#EJERCICIO 3
i = 5
f = 6.5

i_to_f = float(5)  # tranformar el entero a flotante
f_to_i = int(6.5)  # tranformar el flotante a entero

print(f'\nEjercicio 3\nEntero -> Valor Original: {i}, Conversión a Flotante: {i_to_f}')
print(f'Flotante -> Valor Original: {f}, Conversión a Flotante: {f_to_i}')


