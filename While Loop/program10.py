#write a python program to check whether a number is prime or not
n=int(input("Enter a number: "))
i=2
is_prime=True
while i<n:
    if n%i==0:
        is_prime=False
        break
    i+=1
if is_prime:
    print("The number is prime")
else:
    print("The number is not prime")