import time
leds = [37,35,33,31]
pulsador = 23 
chan_list= [leds]
numero = 0

def binario(numero):
    return bin(numero)[2:].zfill(4)

while True:
    print ("------")
    time.sleep(2)
    bnumero = binario(numero)
    if numero == 9:
        numero = 0
    else:
        numero = numero + 1
    for b in range(4):
        led = leds[b]
        valor = int(bnumero[b])
        print(valor)
         

