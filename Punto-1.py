print("Bienvenido al programa para calcular su IMC")
persona={"Nombre:": "","Apellido:": "","Edad:": "","Peso en Kg:": 0,"Altura en Mts:": 0,"Dirección:": "","Teléfono:": ""}

def cat_imc(imc):
    if imc < 18.5:
        print("Su IMC corresponde a la categoria de Bajo Peso")
    elif imc < 24.9:
        print("Su IMC corresponde a la categoria de Peso Normal")
    elif imc < 29.9:
        print("Su IMC corresponde a la categoria de Sobre Peso")
    elif imc < 34.9:
        print("Su IMC corresponde a la categoria de Obesidad tipo I")
    elif imc < 39.9:
        print("Su IMC corresponde a la categoria de Obesidad tipo II")
    elif imc > 40:
        print("Su IMC corresponde a la categoria de Obesidad tipo III")

def imprimir ():
    for dato in persona:
        print (dato, persona[dato])

for a in persona:
    persona[a]=input(f"Complete con su {a}")

imc=round(float(persona["Peso en Kg:"]) / (float(persona["Altura en Mts:"])**2),2)

persona["IMC"]=imc
imprimir()
cat_imc(imc)







