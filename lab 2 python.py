# QUESTION1
l=float(input("enter the length:"))
w=float(input("enter the width"))
a=l*w
print("area is:",a)

# QUESTION 2
l=float(input("enter the length:"))
w=float(input("enter the width:"))
area=(l*0.3048)*(w*0.3048)
print("area is:",area)

QUESTION 3
x=int(input("enter the of x:"))
y=int(input("enter the of y:"))
if x<0 or y<0:
    print("invalid input") 
elif y%x==0:
    print("y is divisible by x")
    print(y,"is dividible by",x)
else:
    print("y is not divisible by x")

QUESTION 4
x=int(input("enter the no.;"))
if x/2>=0:
    print("no. is even")
else:
    print("no. id odd")

QUESTION 5
r=int(input("enter the radius:"))
area=(22/7)*r**2
if r>1 and r<100:
    print("area of the circle is",area,"centimeter square")

else:
    print("enter the correct radius")

QUESTION 6
x=float(input("enter the temperature (`c):"))
f=x*(9/5)+32
if x>=0 and x<=100:
    print("temperature in fahrenheit:",f)
else:
    print("enter the temperature between 1 to 100")

QUESTION7
year=int(input("Enter the year(in 4 digit):"))
if year>0:
  if year%4==0:
    print("Enter Year(",year,") is a lear year ")
  else:
    print("Enter Year is not a leap year")
elif (year<=0):
  print("Enter the valid year")
else:
  print("you can try again")

QUESTION 8
p=int(input("enter the amount:"))
t=int(input("enter the time(in months)"))
t_1=t/12
if p<500 or t<6:
  print("enter the minimun time and principle")
elif p>=500 and t>=6:
  si=(p*7.1*t_1)/100
  print("intrest is",si)
else:
  print("enter the right value")

QUESTION 9
p=int(input("enter the amount:"))
t=int(input("enter the time(in months)"))
t_1=t/12
if p<500 or t<6:
  print("enter the minimun time and principle")
elif p>=500 and t>=6:
  s=(p*7.1*t_1)/100
  print("intrest is",s)
else:
  print("enter the right value")

QUESTION 10
time=int(input("Enter the seconds in the range of 1 to 86400:"))
hour=int(time/3600)
a=hour*3600
minute= int((time-a)/60)
b=minute*60
second=(time - a - b )
if time>=0:
    print("your given number in seconds converted into hour:minute:second",hour,":",minute,":",second)
else:
    print("please, entered the second in the given range")



