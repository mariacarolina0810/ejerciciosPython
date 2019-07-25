edad= int(input("Digite su edad"))
genero= input ("Digite sexo, H para hombre, M para mujer")

if edad>=18:
    if genero in'Hh':
       print ("Señor usted es mayor de edad")
    elif genero in 'Mm':
        print ("Señora, usted es mayor de edad")
    else:
        print("Dato incorrecto")
else:
    if genero in'Mm':
         print ("Señorita usted es menor de edad")
    elif genero in'Hh':
        print ("Señor, usted es menor de edad")
    else:
        print("Dato incorrecto")

   

    
