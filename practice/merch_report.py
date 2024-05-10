from random import randint


print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep="")


otp2= ''.join(str(randint(0,9)) for _ in range(6))
print(otp2)


otp = ''.join(str(randint(0, 9)) for _ in range(6))
print(otp)