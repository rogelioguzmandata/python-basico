empleados = [
    "A1234"
    "O9981"
    "G5566"
    "X1111"
    "A7777"
]
administrativos = 0
operarios = 0
gerentes = 0
invalidos = 0
for codigo in empleados:
    letra = codigo [0]
    if letra == "A":
        administrativos += 1
    elif letra == "O":
        operarios += 1
    elif letra == "G":
        gerentes += 1
    else:
        invalidos += 1
reporte = f'''
Administrativos: {administrativos}
Operarios: {operarios}
Gerentes: {gerentes}
Invalidos: {invalidos}
total_procesados: {len(empleados)}
'''
print(reporte)