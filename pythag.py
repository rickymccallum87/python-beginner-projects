print('Welcome to Pythagorean Triples Checker')

# Loop to check multiple triangles
while True:
  # Request sides from user
  print('Enter lengths of 3 sides. Enter 0 to exit.')
  a = float(input('Side A: '))
  if a == 0:
    break
  b = float(input('Side B: '))
  c = float(input('Side C: '))

  # Make sure Side C is the longest
  if a > c:
    a, c = c, a
  if b > c:
    b, c = c, b

  # Check for Pythagorean Triple
  if a ** 2 + b ** 2 == c ** 2:
    triple = True
  else:
    triple = False

  # Print result
  print('Pythagorean Triple: ', triple)
