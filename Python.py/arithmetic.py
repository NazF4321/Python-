#program to enter two numbers and perform all arithmetic operations
print("enter any two positive integer numbers:")
p, q = int(input()), int(input())
sum, sub, mul, mod, div = 0, 0, 0, 0
sum = p + q
sub = p - q
mul = p * q
div = p / q
mod = p % q
print("sum ",p," + ",q," = ",sum)
print("The value of sub is ",sub)
print("The value of mul is ",mul)
print("The value of div is ",div)
print("The value of mod is ",mod)
