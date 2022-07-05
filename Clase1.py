print ('"Estoy"\n"Aprendiendo"\n"Python" ')
# Resulve la multiplicacion y printea en la consola
diez = 10
tres = 3.5
resultado = diez * tres
print ('Este es el resultado de la multiplicacion: ', resultado)

# Creamos funciones aritmeticas (+, -, * y /)
# Y la representamos en la consola con sus respectivos resultados
def  sumar(numero1, numero2):
    return(numero1 + numero2)
print ('Este es el resultado de la suma: ',sumar(diez, tres))
def resta(numero1, numero2):
    return numero1 - numero2
print('Este es el resultado de la resta: ',resta(diez, tres))
def multiplicar(numero1, numero2):
    return numero1 * numero2
print('Este es el resultado de la multiplicacion: ',multiplicar(diez, tres))
def division(numero1, numero2):
    return numero1 /numero2 
print('Este es el resultado de la division: ',division(diez, tres))   

# Utilizando la funcion if - else -
operador = '+'
if (operador == "+"):
    resultado = sumar(diez, tres);
print('El resultado del operador', operador,'es: ', resultado )
    
    
    