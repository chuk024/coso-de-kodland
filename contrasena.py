import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("de cuantos caracteres quiere la contraseña"))
contra = ""
for i in range(longitud):
    coso = random.choice(caracteres)
    contra += coso
print(contra)
