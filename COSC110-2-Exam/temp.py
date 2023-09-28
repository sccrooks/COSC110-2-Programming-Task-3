def mystery(num1, num2, depth):
  print("\nn1: " + str(num1))
  print("n2: " + str(num2))
  print("d: " + str(depth))

  if num1 == num2:
    return num1
  if num1 > num2:
    return mystery(num2, num1, depth+1)
  if num2 % 5 == num1 % 5:
    return mystery(num1, num2//2, depth+1)


  return mystery(num1, num2 + 1, depth+1)

value = mystery(8, 5, 0)
print(value)