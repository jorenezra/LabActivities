def make_exponentiater(exponent):
  return lambda(x): pow(x,exponent)
  
square = make_exponentiater(2)
cube = make_exponentiater(3)

print (square(4))
print (cube(4))
