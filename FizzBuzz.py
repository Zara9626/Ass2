# Created by Zarifa Ishankhodjaeva 
# For FSAD bootcamp 
# Assignment2

def fizz_buzz():
  for x in range(1, 100):
      if ( x % 5 ==0) and (x% 3 ==0):
          print ("FizzBuzz")
      elif x % 5==0:
          print("Buzz")
      elif (x% 3 ==0):
          print ("Fizz")
      else:
          print(x)


def primes(p):
    for num in range(2 ,p):
        num>1
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print("Prime numbers are " ,num)



def prime_factorization(num1):   ## it is working somehow, but I would do it in recursion rather than loops
    list = []
    while(num1 % 2==0):
        list.append("2")
        num1=num1//2
        while num1 % 3 ==0 :
            list.append("3")
            num1=num1//3
            while num1 % 5 ==0 :
                list.append("5")
                num1=num1//5
                print(list)


    




fizz_buzz()                    #calling functions

p = int(input("Enter a number:"))
primes(p)
num1 = int(input("ENTER A NUMBER : "))
prime_factorization(num1)


        



