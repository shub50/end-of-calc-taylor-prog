#program used for estimating value of function using any order taylor polynomial
import math

if __name__ == '__main__':
    data = {}
    data['coefficients'] = ''
    data['derivative'] = ''
print('If there is a sinx function input it as sin(x)')
print('If there is a cosx function input it as cos(x)')
print('If there is a tanx function input it as tan(x)')
print('If there is a cotx function input it as cot(x)')
print('If there is a secx function input it as sec(x)')
print('If there is a cscx function input it as csc(x)')
print('If there is a log(x)/log(base) function input it as log(x[,base]')
print('If there is an lnx function input it as log(x)')
print('If there is a e^x function input it as exp(x)')
print('If there is a a^x function input it as pow(a,x)')
print('If there is an inverse sin(x) function input it as asin(x)')
print('If there is an inverse cos(x) function input it as acos(x)')
print('If there is an inverse tan(x) function input it as atan(x)')
print('If there is an inverse cot(x) function input it as acot(x)')
print('If there is an inverse sec(x) function input it as asec(x)')
print('If there is an inverse csc(x) function input it as acsc(x)')
print('Input x^ as x**')
print('Use the * to show multiplication. Ex: 3x^2 is 3*x**2')

function = input('Enter the function: ')
center = int(input('Enter the center: '))
order = int(input('Order of the series: '))
value = float(input('Evaluated at: '))

derivs = []

#calculates values of original function over interval (center-1,center+1)
range1 = int(2/0.001)
x = float(center-1)
fval = []
deltx = 0.001
tot=0
for i in range(0,range1):
    tot=float(eval(function))
    fval.append(tot)
    x+=0.001
n=0
derivs.append(fval)

for i in range(0,order):
    fval = []
    valfval = 0.0
    for i in range(0,len(derivs[n])-1):
        valfval = (derivs[n-1][i+1]-derivs[n-1][i])/deltx
        fval.append(valfval)
    n = n+1
    if fval[1000] == 0:
        break
    derivs.append(fval)

f = 0 
fn = []
for i in range(0,len(derivs)):
    f = derivs[i][1000]
    fn.append(f)
fi = 0
d=0
ci = []
for i in range(0,len(fn)):
    l = fn[i]/(math.factorial(i))
    ci.append(l)

tl = []
for i in range(0,len(fn)):
    if i == len(fn)-1:
        tlv = str("(")+str(ci[i])+str("*(x-")+str(center)+str(")**")+str(i)+str(")")
    else:
        tlv = str("(")+str(ci[i])+str("*(x-")+str(center)+str(")**")+str(i)+str(")+")
    tl.append(tlv)
eq = 1
for i in range(0,len(fn)):
    if i == 0:
        eq = str(tl[i])
    else:
        eq = str(eq) + str(tl[i])

print(str("Taylor series of order ")+str(order)+str(": ")+str(eq))

fvalue = []
for i in range(0,len(fn)):
    valuef=ci[i]*((value-center)**i)
    fvalue.append(valuef)

estimate = sum(fvalue)
print(str("f(")+str(value)+str("): ")+str(estimate))
