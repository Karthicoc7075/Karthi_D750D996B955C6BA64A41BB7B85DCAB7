def factorial(num):
  if num == 0 or num == 1:
    return 1
  else:
    return num * factorial(num - 1)


number = int(input("Enter the value:"))
result = factorial(number)

print("The factorial of {} is {}".format(number,result))
