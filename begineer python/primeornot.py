num = int(input("Enter a number: "))
prime = True

for i in range(2,num):
    if(num%i==0):
        prime = False

if prime:
    print("The number is prime.")
else:
    print("The number is composite")