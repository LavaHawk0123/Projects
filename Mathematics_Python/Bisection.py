import math
import sys
#Class to find one root of the given equation using False Position

class Bisectionfinal:

#Function to initialise polynomial
 def Initialise(self):
        self.coeff_xf = input("Enter coefficiant of x^4: ")
        self.coeff_xc = input("Enter coefficiant of x^3: ")
        self.coeff_xs = input("Enter coefficiant of x^2: ")
        self.coeff_x = input("Enter coefficiant of x: ")
        self.const = input("Enter constant value: ")
        self.coeff_cos = input("Enter coefficiant of cosx: ")
        self.coeff_sin = input("Enter coefficiant of sinx: ")
        self.coeff_tan = input("Enter coefficiant of tanx: ")
        self.e = input("Enter tolerable error: ")

#Function to find value of function for a value of x

 def Func(self,x):
        self.func_value = (self.coeff_xf * (x**4))+(self.coeff_xc * (x**3))+(self.coeff_xs * (x**2))+(self.coeff_x * (x))+ self.const+ (self.coeff_cos*(math.cos(x)))+(self.coeff_sin*(math.sin(x)))+(self.coeff_tan*(math.tan(x)))
        return self.func_value


#Function to find initial values of a and b

 def starter(self):
        for x in range(-10,10):
            if (self.Func(x)*self.Func(x-1))<0:
                a = x-1
                b=x
                break
        return a,b

#Function to find value of x for a given value of a,b

 def X_Value(self,a,b):
        sum = (a+b)
        x_i = sum/2
        return x_i

#Function to compute the value of f(a) and f(b) as well as change the limits

 def Lim(self,x_i,a,b):
        if self.Func(x_i)>0:
            b = x_i
            print("Since the value is greater than 0, We replace the upper limit of the interval")
        elif self.Func(x_i)<0:
            a = x_i
            print("Since the value is lesser than 0, We replace the lower limit of the interval")
        else:
            print("The root is : "+str(x_i))
            sys.exit(0)
        return b,a
 def Temp_x(self,a):
     temp_a = a
     return temp_a


#Main Function to carry out False Position method 

 def Bisection(self):
  self.Initialise()
  print("\n"+"The Equation is f(x) = ("+str(self.coeff_xc) +") x^3+ ("+str(self.coeff_xs) +") x^2+ ("+str(self.coeff_x )+") x+( "+ str(self.const)+")+ ("+ str(self.coeff_cos)+")cos(x)+ ("+str(self.coeff_sin)+")sin(x)+ ("+str(self.coeff_tan)+")tan(x)"+"\n")
  a,b = self.starter()
  waste1=0
  print("\n")
  print("Initial value of (a,b) = ("+str(a)+","+str(b)+").")
  for i in range(1,15):
   x = self.X_Value(a,b)
   print("Iteration "+str(i)+":"+"\t")
   print("Value of x is "+str(x)+" and f(x) = "+str(self.Func(x))+"\t")
   b,a = self.Lim(x,a,b)
   print("Now, the roots lie between  ("+str(a)+","+str(b)+").")
   waste1 = self.Temp_x(x)
   print("\n")
  root=x
  return root


#Main function call

Eqn1 = Bisectionfinal()
root_final = Eqn1.Bisection()
print("\n\nThe root is : "+str(root_final))