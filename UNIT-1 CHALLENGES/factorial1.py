def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)
n=int(input("enter the num:"))
print("the factorial of the number is:",factorial(n))
