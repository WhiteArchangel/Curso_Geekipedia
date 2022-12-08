#Números int y long
#Los números Enteros (int) y los números Largos (long) no tienen parte decimal, sólo entera, aunque no se ocuparán los tipo long ya que son de extrema rareza en programas simples.
numero_entero = 10
#Para poder determinar el tipo de dato, se debe ocupar la función "type()" que permite identicarlo durante la impresión de éste sobre la variable.
print(numero_entero, type(numero_entero))
#Cabe destacar que la coma que se utiliza dentro de print que hace la función de agregación de variables dentro de éste y es capaz de imprimirlo como str.

#Números float
#Los números Flotantes o Reales tienen parte decimal, se expresa como float.
numero_flotante = 55.5
print(numero_flotante, type(numero_flotante))

#Números complejos
#Aquellos números que tienen una parte real y una imaginaria, aunque son extraños en la programación básica y algo avanzada.
numero_complejo = 5 + 5j
print(numero_complejo, type(numero_complejo))

#Cadenas o Strings
#Son textos entre comillas y serán asignados tanto a variables como dato o como comentario.
texto_a = "Este es un dato de tipo string."
print(texto_a, type (texto_a))

#Booleanos
#Teniendo dos valores únicos: True o False, usados en expresiones condicionales y bucles, expresados con bool, un ejemplo de booleanos es la comparación.
mensaje_a = "Tipos de datos"
mensaje_b = "Tipos de datos"
mensaje_c = mensaje_a == mensaje_b
print(mensaje_c, type(mensaje_c))
#El código anterior será True.
mensaje_aa = "True"
mensaje_bb = "False"
mensaje_cc = mensaje_aa == mensaje_bb
print(mensaje_cc, type(mensaje_cc))
#El valor anterior será False.
#Añadiendo algo más, se puede simplificar como:
mensaje_finaltrue = 5 == 5
print(mensaje_finaltrue, type(mensaje_finaltrue))
mensaje_finalfalse = "a" == "b"
print(mensaje_finalfalse, type(mensaje_finalfalse))
