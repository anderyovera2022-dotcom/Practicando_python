#Genera una tabla de multiplicar 
numero = int(input("Ingresa el numero a multiplicar: "))
for i in range(0,13):
    print(f"{numero} x {i} = {numero*i}")
