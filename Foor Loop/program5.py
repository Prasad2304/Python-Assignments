#write a python program to sum the given sequence 1+1/1!+1/2!+1/3!+...+1/n!
n=int(input("Enter a number: "))
sum=0
for i in range(1, n+1):
    fact=1
    for j in range(1, i+1):
        fact*=j
    sum+=1/fact
print("Sum of the sequence is:", sum)