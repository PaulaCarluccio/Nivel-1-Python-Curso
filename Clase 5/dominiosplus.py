dominios = ["https://damiandeluca.com.ar","https://itmaster.com.ar","https://www.mentesliberadas.com/","http://ar.testing.org","https://google.com.ar","http://test.net"]
for dominio in dominios:
    if dominio.lower().startswith("https://") and dominio.lower().endswith(".ar"):
        print(dominio)