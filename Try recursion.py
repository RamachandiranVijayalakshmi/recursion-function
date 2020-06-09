def tri_recursion(a):
  if(a > 0):
    option = a + tri_recursion(a- 1)
    print(option)
  else:
    option = 0
  return option

print("\n\nRecursion Example Results")
tri_recursion(5)
