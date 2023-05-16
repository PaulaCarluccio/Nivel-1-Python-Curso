var1 = "Algo"
if 'var1' in vars() or 'var1' in globals():
    print("existe")
else:
    print("no existe")