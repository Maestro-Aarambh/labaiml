import math
class Power:
    def power(self,n):
        num=int(input("Enter power to be raised "))
        result=pow(n,num)
        print(n,"raised to power",num ,"is",result)
exponent=Power()
n=int(input("Enter a number "))
exponent.power(n)