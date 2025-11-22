empleado = "Roberto Roena"
sucursal = "Valencia Norte"
producto_1 = "Laptop HP"
producto_2 = "Teclado Mecánico"
producto_3 = "Monitor 24 pulgadas"
venta_1 = 689.99
venta_2 = 45.50
venta_3 = 129.90
iva = 0.21
comision = 0.05
subtotal = venta_1 + venta_2 + venta_3
impuesto = subtotal * iva
total = subtotal + impuesto
comision_final = total * comision
dia_bueno = total > 700
print("---- Datos iniciales ----")
print("Empleado:", empleado)
print("Sucursal:", sucursal)
print("Ventas:", producto_1, producto_2, producto_3, sep=" | ")
print("\n------ Cálculos ------")
print("Subtotal:", subtotal)
print("Impuesto (IVA):", impuesto)
print("Total recaudado:", total)
print("Proceso comisión...", end=" ")
print("completado!")
reporte = f"""
========== REPORTE FINAL ==========
Empleado: {empleado} 
Sucursal: {sucursal}
Ventas del día:
- {producto_1}: {venta_1:.2f} $
- {producto_2}: {venta_2:.2f} $
- {producto_3}: {venta_3:.2f} $
Subtotal: {subtotal:.2f} $
IVA (21%): {impuesto:.2f} $
Total: {total:.2f} $
Comisión del empleado (5%): {comision_final:.2f} $
¿Día bueno?: {dia_bueno}
===================================
"""
print(reporte)