x=int(input('Enter a four digit number'))
a=x//1000
b=x//100 -10*a
c=x//10 -100*a-10*b
d=x-1000*a-100*b-10*c
if (a+b==c+d):
    print("F")
else:
    print("U")