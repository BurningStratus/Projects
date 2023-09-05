
mem = []
numn = input("Number: ")

while numn != "":
    numn = int(numn)
    mem.append(numn)
    numn = input("Nombre: ")

else:
    mem.sort(reverse=True)
    print(mem[0:5])