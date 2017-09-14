a = int(input(""))
if a > 0 and a < 1000000:
    print a
    valor = (a) / 100
    print '%d nota(s) de R$ 100,00' %valor
    a = a - valor*100 
    valor = a/50
    print '%d nota(s) de R$ 50,00' %(valor)
    a = a - valor*50
    valor = a/20
    print '%d nota(s) de R$ 20,00' %(valor)
    a = a - valor*20
    valor = a/10
    print '%d nota(s) de R$ 10,00'%(valor)
    a = a - valor*10
    valor = a/5
    print '%d nota(s) de R$ 5,00' %(valor)
    a = a - valor*5
    valor = a/2
    print '%d nota(s) de R$ 2,00'%(valor)
    a = a - valor*2
    valor = a/1
    print '%d nota(s) de R$ 1,00'%(valor)
else:
    'Presentation Error'