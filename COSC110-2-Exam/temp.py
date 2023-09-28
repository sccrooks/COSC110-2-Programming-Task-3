def mystery(num1, num2, c):
  print("n" + str(c) +": " + str(num1))
  c += 1
  print("n" + str(c) + ": " + str(num2))
  c+=1

  if num1 == num2:
    return num1
  if num1 > num2:
    value = mystery(num2, num1, c)
    print("VALUE:" + str(value))
    return value
  if num2 % 5 == num1 % 5:
    value = mystery(num1, num2//2, c)
    print("VALUE:" + str(value))
    return value

  value = mystery(num1, num2 + 1,c )
  print("VALUE:" + str(value))
  return value

value = mystery(8, 5, 1)
print(value)