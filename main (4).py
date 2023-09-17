# QUESTION1
X = float(int(input(" enter first side of trapezoid")))
Y = float(int(input("Enter second side of trapezoid")))
H = float(int(input("enter height of trapezoid  ")))
p = X+Y
print(p/2*H)
 

W = float(int(input("Enter the weight(in kg):")))
H = float(int(input("Enter the height(in M)")))
BMI =W/(H**2)  
print("body mass index is",BMI)

# QUESTION2
W = float(int(input("Enter the weight(in pound):")))
H = float(int(input("Enter the height(in M)")))
BMI = (W/0.45)/((H/39.3)**2)
print("body mass index is",BMI)

# QUESTION3
side1 = input("Enter the first side of triangle")
side2 = input("Enter the second side of triangle")
side3 = input("enter the third side of the triangle")
if((side1+side2) > side3):
  if((side1==side2)and(side2==side3)and(side3==side1)):
    print("they form equlateral triangle")
  else:
    print("they form triangle")
else:
  print("they cannot form triangle")

# QUESTION4
abc = int(input("enter the three digitr number"))
ones  = abc % 10
tens  = (abc % 100) // 10
hundreds  = (abc%1000) // 100
sum = ones +tens + hundreds
print("sum of three digits is :", sum)
if sum % 3==0:
  print("number is divisible by 3")

else:
  print("number is not divisibe by 3")

# QUESTION5
digit = int(input("enter the 5 digit noi:"))
a = (digit%10)//1
b = (digit%100)//10
c = (digit%1000)//100
d = (digit%10000)//1000
e = (digit%100000)//10000
if(a==e and b==d and c==c):
  print("entered number is palindrome")
else:
  print("enterd number is not palindrme")



# QUESTION6
print("enters number will be swap the value")
x = input("Enter the first value:")
y = input("Enter the second value:") 
A = y
B = x 
print("A is" ,A)
print("B is" , B)


# QUESTION7
X = int(input("enter the real part of first complex number"))
Y = int(input("enter the imaginary part of first complex no."))
X1 = int(input("enter the real part of second complex no."))
Y1 = int(input("enter the imaginary part of second complex n"))
com_1 = complex(X,Y)
com_2 = complex(X1,Y1)
print(com_1+com_2)
print(com_1*com_2)

# QUESTION8
salary = float(input("enter your basic salary:"))
HRD = salary*(20/100)
TA = salary*(5/100)
DA = salary*(10/100)
GROSS_SLARY = salary +HRD +TA + DA
print("your gross salary is equal to",GROSS_SLARY)


