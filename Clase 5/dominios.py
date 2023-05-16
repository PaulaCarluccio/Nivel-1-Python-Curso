dominios = ["https://damiandeluca.com.ar","https://itmaster.com.ar","https://www.mentesliberadas.com/","http://ar.argentina.org","https://google.com.ar"]
for dominio in dominios:
    if dominio[-3:].lower() == ".ar":
        print(dominio)