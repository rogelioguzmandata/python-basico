precio= 1250000
iva=25
descuento= 12
iva_numero= precio *(iva/100)
total_con_iva= precio+iva_numero
descuento_numero=total_con_iva*(12/100)
total_con_descuento=total_con_iva-descuento_numero
print(total_con_descuento)