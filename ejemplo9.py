class Empleado:
     def __init__(self):
        self.codigo = 0
        self.nombre = ""
        self.apellido = ""
        self.salario_base = ""

        def retencion(self):
            ret=(self.salario_base)*0.10
            return ret
        
        def nombre_completo(self):
            print (self.nombre+" "+ self.apellido)

        def calcular_salario_neto(self):
            smmlv=828116
            Aux=97032
            if (self.salario_base<=smmlv):
                neto=self.salario_base+Aux
                print (neto)
            else:
                neto=self.salario_base
                print (neto)
            
emp=Empleado()
emp.codigo=int(input("Digite su codigo"))
emp.nombre=input("Digite su nombre")
emp.apellido=input("Digite su apellido")
emp.salario_base=int(input("Digite su salario base"))

print(emp.retencion())
print(emp.nombre_completo())
print(emp.calcular_salario_neto())
    

    

   
