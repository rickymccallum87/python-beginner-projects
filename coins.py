import copy

# A reference dictionary
#                  coin: [weight, count, wrapper, value]
reference = { 'pennies': [   2.5,     0,      50,   .01],
              'nickels': [   5.0,     0,      40,   .05],
                'dimes': [ 2.268,     0,      50,   .10],
             'quarters': [  5.67,     0,      40,   .25]}

# The user's data, with default values from the reference
onHand = copy.deepcopy(reference)
count = 0
value = 0.0


# Convert reference weights to pounds, if desired
mass = input('Are your weights in grams (g) or pounds (lb)?')
if mass == 'lb' or mass == 'pounds':
  for k in reference:
    reference[k][0] /= 453.59237


# For each coin type,
for k in reference:
  # ask the weight,
  onHand[k][0] = float(input(('Weight of ' + k + ': ').ljust(20)))

  # and use that to calculate the count, wrappers, and value
  onHand[k][1] = int(onHand[k][0] / reference[k][0]) # round count down
  onHand[k][2] = int(onHand[k][1] / reference[k][2]) # round wrappers down
  onHand[k][3] = float(onHand[k][1] * reference[k][3])

  # Add to totals
  count += onHand[k][1]
  value += onHand[k][3]


# Print results for each coin type,
for k in onHand:
  print('')
  print(k.capitalize().center(20))
  print('Wrappers:'.rjust(10), str(onHand[k][2]))
  print('Count:'.rjust(10), str(onHand[k][1]))
  print('Value:'.rjust(10), '${:,.2f}'.format(onHand[k][3])) # round value to cents

# and total results
print('')
print('Total'.center(20))
print('Count:'.rjust(10), str(count))
print('Value:'.rjust(10), '${:,.2f}'.format(value)) # round value to cents
