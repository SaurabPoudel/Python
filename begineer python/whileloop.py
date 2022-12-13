#pallindrome or not
n = int(input("Enter a number: "))
temp = n
rev = 0
while n!=0:
    a = n % 10
    rev = rev*10 + a
    n = n // 10
if rev == temp:
    print("Pallindrome")
else:
    print("Not Pallindrome")