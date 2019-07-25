num1=int(input("Digite el primer numero: "))
num2=int(input("Digite el segundo numero: "))
operacion=int(input("Digite 1 para sumar, 2 para restar, 3 para multiplicar, 4 para dividir: "))
if operacion==1:
    print("La suma es: ", (num1+num2))
elif operacion==2:
     print("La resta es: ", (num1-num2))
elif operacion==3:
     print("La multiplicacion es: ", (num1*num2))
elif operacion==4:
     print("La resta es: ", (num1/num2))
else:
    print("Por favor digite un valor correcto para la operacion")
    
    
    

