num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
operador = input("ingrese el operador (suma|resta): ")

if (operador == "suma"):
    res = num1 + num2
elif(operador == "resta"):
    res = num1 - num2
else:
    print("no existe operador0")
    exit()



print("el resultado final es "+str(res))