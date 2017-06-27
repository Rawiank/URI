vetor = [0,1]
contador = 2

while contador < 61:
    vetor.append(long(vetor[contador-2] + vetor[contador-1]))
    contador+=1

t = int(input(""))

contador = 0
if t!=2:
    while contador < t:
        n = int(input(""))
        print "Fib(%d) = %d" %(n,vetor[n])
        contador +=1