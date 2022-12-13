def sumofdigits(x):
  sum = 0
  while(x !=0):
    a = x % 10
    sum = sum + a
    x = x // 10
  print(sum)
sumofdigits(123)
