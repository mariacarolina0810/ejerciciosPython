peso=float(input("Digite su peso"))
estatura=float(input("Digite su estatura"))
imc=peso/estatura**2

if imc<18.5:
    print (imc, " Esta bajo de peso")
elif imc>=18.5 and imc <24.9:
     print (imc, " su peso es normal")
elif imc>=25 and imc <29.9:
     print (imc, " se encuentra en sobrepeso")
elif imc>=30 and imc <34.9:
     print (imc, " se encuentra en obesidad I")
elif imc>=35 and imc <39.9:
     print (imc, " se encuentra en obesidad II")
elif imc>=40 and imc <49.9:
     print (imc, " se encuentra en obesidad III")
else:
     print (imc, " se encuentra en obesidad IV")
    
