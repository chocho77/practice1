def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
print("--")
tri_recursion(-1)
print("--")
tri_recursion(0)
print("--")
tri_recursion(1)
print("--")
tri_recursion(2)
print("--")
tri_recursion(23)
print("--")
