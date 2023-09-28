def mystery(num1, num2):
  print("n1: " + str(num1))
  print("n2: " + str(num2))

  if num1 == num2:
    return num1
  if num1 > num2:
    return mystery(num2, num1)
  if num2 % 5 == num1 % 5:
    return mystery(num1, num2//2)

  
  return mystery(num1, num2 + 1)

value = mystery(8, 5)
print(value)