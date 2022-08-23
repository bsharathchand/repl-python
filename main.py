def myfunc():
  print ('sharath')
  print ('sudha')


if __name__ == "__main__":
    myfunc ()

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(10))