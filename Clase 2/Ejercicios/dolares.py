#dada la variable precio_en_dolares con un valor con punto flotante en dólares
#y otra variable cotización (67).
#Calcular su valor en pesos argentinos y su valor en pesos argentinos
#con el adicionado del impuesto del 30%.

precio_en_dolares = 100
cotizacion = 67
alicuota = 30
precio_en_pesos = precio_en_dolares * cotizacion
impuesto = ((precio_en_dolares * cotizacion) * alicuota) / 100
precio_total_en_pesos = precio_en_pesos  + impuesto
print(precio_total_en_pesos)