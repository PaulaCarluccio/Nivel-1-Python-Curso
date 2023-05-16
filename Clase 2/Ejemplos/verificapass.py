print("Indique Password")
password = input()
print("Confirme Password")
cpassword = input()
if password.lower() == cpassword.lower():
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas NO coinciden")