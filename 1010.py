aPagar = 0
for i in range(0,2):
    lista = raw_input("").split(" ")
    aPagar = aPagar + (int(lista[1])* float(lista[2]))
print 'VALOR A PAGAR: R$ %.2f' %(aPagar)


