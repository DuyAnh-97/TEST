import sys

print(sys.executable)

name = input("Your name ? ")
print("Hello,", name)

def fib(n):
    a , b = 0 , 1
    while a < n:
        print(a)
        a, b = b, b + a

fib(60) 

a = "Day la test"

b = 123