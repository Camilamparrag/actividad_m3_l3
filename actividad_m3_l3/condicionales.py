#1. decision simple

edad = int(input("ingresa tu edad:"))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#2. decision multiple con elif

nota =int(input("Ingresa calificacion:"))

if nota == 7:
    print("Excelente")

elif nota == 6:
    print("Muy bien")

elif nota == 5:
    print("Bien")

elif nota == 4:
    print("Suficiente")

else:
    print("Insuficiente")

#3. condicion anidadas

numero = int(input("Ingresa un numero:"))

if numero >= 0:
    if numero == 0:
        print("Es cero")
    else:
        print("Numero positivo")
else:
    print("numero negativo")

#4. condicion de borde

#se solicita la eleccion de numero, se convierte la entrada a entero para poder compararlo
#se utiliza eleccion_numero como nombre de varibale (snake_case)
eleccion_numero = int(input("Ingresa un numero de 1 al 100:")) 

#bloque para verificar si el numero es exactamente uno de los limites (1 a 100)
if eleccion_numero == 1 or eleccion_numero == 100: 
    print("Estas en el limite permitido")

#bloque para verificar si esta dentro del rango (2 a 99)
elif 1 < eleccion_numero < 100: 
    print("Dentro del rango")

#bloque para numero que no esten dentro de 1 al 100
else:                           
    print("Fuera de rango")