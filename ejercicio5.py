nombre_completo = "Roberto Roena"
edad = 27
salario_base = 1200.50
bono_anual = 1.5e2
print("TIPOS DE DATOS")
print(type(edad))
print(type(salario_base))
print(type(bono_anual))
print("------------------------")
print("PRIMERAS LETRAS DEL NOMBRE")
print(nombre_completo[0])
print(nombre_completo[1])
print(nombre_completo[2])
print("------------------------")
salario_total = salario_base + bono_anual
print("CÁLCULOS SALARIALES")
print("salario base", salario_base)
print("Bono anual", bono_anual)
print("Salario total", salario_total)
print("------------------------")
mayor_de_edad = edad >= 18
es_jefe = False
print("DATOS BOOLEANOS")
print("¿Es mayor de edad?", mayor_de_edad)
print("¿Es jefe del área?", es_jefe)
print(type(mayor_de_edad))
print(type(es_jefe))
print("------------------------")
reporte = f"""
REPORTE DEL EMPLEADO
------------------------
Nombre: {nombre_completo}
Edad: {edad}
Salario total anuel: {salario_total}$
Mayor de edad: {mayor_de_edad}
¿Es jefe?: {es_jefe}
Primera letras del nombre: {nombre_completo[0]} {nombre_completo[1]} {nombre_completo[2]}
"""
print(reporte)