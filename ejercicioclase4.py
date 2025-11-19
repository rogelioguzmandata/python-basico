nombres= [
"  Rogelio   Guzman ",
" Maria  Torres   ",
"   Alberto     Pederalba",
"   Pedro  Caval "
]
for nombre in nombres :
    limpio = nombre.strip()
    partes = limpio.split()
    nombre_bonito=" ".join(partes)
    mayusculas = nombre_bonito.upper()
    minusculas = nombre_bonito.lower()
    sin_espacios = nombre_bonito.replace(" ", " ")
    cantidad_letras = len(sin_espacios)
    print("original",nombre)
    print("sin espacios extremos",limpio)
    print("nombre_bonito",nombre_bonito)
    print("mayusculas",mayusculas)
    print("minusculas",minusculas)
    print("letras reales", cantidad_letras)