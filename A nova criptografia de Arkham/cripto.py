from math import sqrt
cont = 0
msg = "Bem vindos ao CTF da Comunidade Alquymia"

e = [num*77 for num in [ord(chr) for chr in msg]]
x = [str(num).replace('0','a').replace('5','r').replace('7','k') for num in e]
l = int(sqrt(len(e)))
print(l)
for i in range(l):
    element = []
    for j in range(l):
        element.append(x[cont])
        cont += 1
    print(element[::-1])