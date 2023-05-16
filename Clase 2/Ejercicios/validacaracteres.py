# pedir usuario y password que cada uno tenga al menos 5 caracteres
# indicar éxito  o errores especificos

print("Usuario:")
usuario = str(input())
print("Contraseña:")
password = str(input())
if len(usuario) < 5 and len(password) < 5:
    print("El usuario y contraseña tiene menos de 5 caracteres")
elif len(usuario) < 5 and len(password) >= 5:
    print("El usuario tiene menos de 5 caracteres")
elif len(usuario) >= 5 and len(password) < 5:
    print("La contraseña tiene menos de 5 caracteres")
else:
    print("Perfecto todo")
        