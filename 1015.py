from math import sqrt
x = raw_input("").split(" ")
y = raw_input("").split(" ")
print '%.4f'%(sqrt(pow(float(y[0])-float(x[0]), 2) + pow(float(y[1])-float(x[1]), 2)))

