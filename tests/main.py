import mi_calculadora

# Operaciones
suma = mi_calculadora.sumar(10, 5)       # 15
resta = mi_calculadora.restar(10, 5)      # 5
multi = mi_calculadora.multiplicar(10, 5) # 50
div = mi_calculadora.dividir(10, 5)       # 2.0
#potencia = mi_calculadora.potenciacion(10, 2)   # 100


#print(f"Suma: {suma}, Resta: {resta}, Multi: {multi}, Div: {div}, Potencia: {potencia}")
print(f"Suma: {suma}, Resta: {resta}, Multi: {multi}, Div: {div}")

# Manejo de errores
try:
    mi_calculadora.dividir(10, 0)
except ValueError as e:
    print(f"Error: {e}") # Error: No se puede dividir por cero.

# Versión
print(f"Versión: {mi_calculadora.__version__}") 
