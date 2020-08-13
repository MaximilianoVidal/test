# n one

vel= int (input("ingrese la cantidad de kilometros que recorre su auto en un dia: "))
cont = vel
ruta= int (input("ingrese los kilometros por recorrer: "))
dia=1

while cont<ruta:
    cont=cont+vel
    dia=dia+1
if cont>=ruta: print ("usted tardara aproximadamente dias",dia)

#n two

a=int (input(print("ingrese lado a: ")))
b=int (input(print("ingrese lado b: ")))
c=int (input(print("ingrese lado c: ")))
if a+b>=c: print("se trata de un triangulo")
else: print("no se trata de un triangulo")
count=0
while count==0:
    if a==b and b==c: print("triangulo equilatero")
    elif a==b or a==c:print("triangulo isoceles")
    else: print("triangulo escaleno")
    count=count+1

#n three

num=1
while num!=0:
   num=int(input("digite un numero: "))
   if num%2==0: print("el numero es par")
   else: print("el numero es impar")
   print ("digite otro numero, o digite 0 para salir")
print("que tenga un buen dia")


#ejercicio supermercado

suma=0
cont=1
print("//para terminar con los productos precione 0")
while cont!=0:
    cont=int(input("ingrese precio del producto: "))
    if cont<0: print("valor no valido")
    else: suma=suma+cont
print("el valor total de su compra es de:",suma)
if suma>=1000:
   total= suma*90/100
   print("con un 10% de descuento el precio final es de:$",total)