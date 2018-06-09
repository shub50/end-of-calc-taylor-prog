#program used for estimating value of function using tenth order taylor polynomial
#note that if consecutive derivatives of f(x) reach 0 before the tenth derivative the estimation may contain large amounts of eror due to limitations of numerical differentiation
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

for i in range(0,order+1):
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
    ci.append(f)

tl = []
for i in range(0,len(fn)):
    tl = str("(x-")+str(center)+str(")**")+str(i)
"""
    fi = str("f")+str(i)+str(": ")
    fl = str(fi)+str(l)
    
#calculates values of each order's taylor coeffecient using consecutive derivatives at the center and the factorial denominator 
I0 = fval[1000]/1
I1 = onederiv[1000]/1
I2 = twoderiv[1000]/2
I3 = threederiv[1000]/6
I4 = fourderiv[1000]/24
I5 = fivederiv[1000]/120
I6 = sixderiv[1000]/720
I7 = sevenderiv[1000]/5040
I8 = eightderiv[1000]/40320
I9 = ninederiv[1000]/362880
I10 = tenderiv[1000]/3628800

C0 = str(fval[1000]/1)
C1 = str(onederiv[1000]/1)
C2 = str(twoderiv[1000]/2)
C3 = str(threederiv[1000]/6)
C4 = str(fourderiv[1000]/24)
C5 = str(fivederiv[1000]/120)
C6 = str(sixderiv[1000]/720)
C7 = str(sevenderiv[1000]/5040)
C8 = str(eightderiv[1000]/40320)
C9 = str(ninederiv[1000]/362880)
C10 = str(tenderiv[1000]/3628800)

print("Coefficients of each order:")
print(str("C0: ")+str(C0))
print(str("C1: ")+str(C1))
print(str("C2: ")+str(C2))
print(str("C3: ")+str(C3))
print(str("C4: ")+str(C4))
print(str("C5: ")+str(C5))
print(str("C6: ")+str(C6))
print(str("C7: ")+str(C7))
print(str("C8: ")+str(C8))
print(str("C9: ")+str(C9))
print(str("C10: ")+str(C10))

tl = []
for i in range(0,len(fn)):
    tlv = str("(x-")+str(center)+str(")**")+str(i)
    tl.append(tlv)

tlval = str(" ")
for i in range(0,len(tl)):
    tfin = str(tl[i]) + tlval 
    if len(tl) != 1 and i != len(tl)-1:
        tfin = tfin + str("+")
    tlval = str(tl[i])
print(tfin)


#calculates value of estimation with Taylor's formula
fvalue = I0*((value-center)**0)+I1*((value-center)**1)+I2*((value-center)**2)+I3*((value-center)**3)+I4*((value-center)**4)+I5*((value-center)**5)+I6*((value-center)**6)+I7*((value-center)**7)+I8*((value-center)**8)+I9*((value-center)**9)+I10*((value-center)**10)

print(str("f(")+str(value)+str("): ") + str(fvalue))"""
