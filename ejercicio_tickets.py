print("=== SISTEMA DE TICKETS ===\n")
cliente = "Roberto Roena"
servicio = "Mantenimiento Premium"
precio_base = 49.99
iva = 0.21
inicial = cliente [0]
precio_iva = precio_base * iva
precio_total = precio_base + precio_iva
es_caro = precio_total > 50
print("Cliente", cliente)
print("Servicio", servicio)
print("Precio base", precio_base)
print("IVA", precio_iva)
print("\n----------------------------------")
print("Cliente", inicial, sep=" -> ")
print("Precio base", precio_base, "IVA", precio_iva, sep=" | ")
print("\n----------------------------------")
print("Generando ticket...", end= " ")
print("¡completado!")
ticket = f"""
==== TICKET DE SERVICIO ====
Cliente: {cliente}
Inicial: {inicial}
Servicio tomado: {servicio}
Precio base: {precio_base} $
IVA (21%): {precio_iva:.2f} $
Total a pagar: {precio_total:.2f} $
¿Es caro?: {es_caro}
=============================
"""
print(ticket)