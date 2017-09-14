valores = raw_input("").split(" ")

maiorAB = (int(valores[0]) + int(valores[1]) + abs(int(valores[0])-int(valores[1])))/2
if maiorAB > int(valores[2]):
    print str(maiorAB) + ' eh o maior'
else:
    print str(valores[2]) + ' eh o maior'