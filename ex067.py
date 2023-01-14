
tabuada = int(input("Quer ver a tabuada de qual valor? "))
while tabuada >= 0:
    for numero in range(1, 11):
        print(f"{tabuada} x {numero} = {tabuada * numero}")
        numero += 1
    tabuada = int(input("Quer ver a tabuada de qual valor? "))