# Permite construir expresiones logicas, se obtiene como resultado un valor booleano.
# Para usarlos deben haber dos operaciones relacionales.

''' Operadores Logicos

and (Conjuncion)
or (Disyuncion)
not (negacion)

'''

# OPERADOR and

resultado = 10 > 3 and 3 < 5
print(resultado)

# Se le conoce como una multiplicacion logica. 
# "True" tiene como valor 1 y "False" tiene como valor 0. Solo si hay dos "True" te suelta como resultado "True".


# OPERADOR or

resultado = 5 > 1 or 3 > 5
print(resultado)

# Se le conoce como una suma logica.
# Solo hace falta que haya un "True" para que te suelte como resultado "True".


# OPERADOR not

resultado = ((3<1) or (5>6))
print(resultado)


resultado = not((3<1) or (5>6))
print(resultado)

# Te suelta como valor el resultado contrario al que te daria la operacion.


''' Prioridad de los operadores en general

1. ()
2. **
3. *, /, modulo, not
4. +, -, and
5. >, <, ==, >=, <=, !=, or 

'''