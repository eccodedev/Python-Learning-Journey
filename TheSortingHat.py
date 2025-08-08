#  The sorting hat: 
  #  This exercise was created to practice the control flow.

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Welcome to the Sorting Hat !!')
print()
print('The Sorting hat is going to ask you some questions and then send you to the right Hogwarts House')
print('Pick a number according to your answer')
print()

flag1 = True
while flag1 == True:
  q1 = int(input('Do you like Dawn or Dusk: \n   1) Dawn \n   2) Dusk \n' ))
  if q1 == 1:
    Gryffindor =  Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
    flag1 = False
  elif q1 == 2:
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
    flag1 = False
  else: 
    print('Wrong input')
    print('Pick the right answer number')
    print()

print()

flag2 = True
while flag2 == True:
  q2 = int(input('When I\'m dead, I want people to remember me as: \n   1) The Good \n   2) The Great \n   3) The Wise \n   4) The Bold \n'))
  if q2 == 1:
    Hufflepuff = Hufflepuff + 2 
    flag2 = False
  elif q2 == 2:
    Slytherin = Slytherin + 2
    flag2 = False
  elif q2 == 3: 
    Ravenclaw = Ravenclaw + 2
    flag2 = False
  elif q2 == 4:
    Gryffindor = Gryffindor + 2
    flag2 = False
  else:
    print('Wrong input')
    print('Pick the right answer number')
    print()

print()

flag3 = True
while flag3 == True:
  q3 = int(input('Which kind of instrument most pleases your ear?: \n   1) The Violin \n   2) The Trumpet \n   3) The Piano \n   4) The Drum \n'))
  if q3 == 1:
    Slytherin = Slytherin + 4
    flag3 = False
  elif q3 == 2:
    Hufflepuff = Hufflepuff + 4
    flag3 = False
  elif q3 == 3:
    Ravenclaw = Ravenclaw + 4
    flag3 = False
  elif q3 == 4:
    Gryffindor = Gryffindor + 4
    flag3 = False

print()

highest_score = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
if highest_score == Gryffindor:
  print('Congratulations you are a Gryffindor!')
elif highest_score == Ravenclaw:
  print('Congratulations you are a Ravenclaw!')
elif highest_score == Hufflepuff:
  print('Hufflepuff!!')
elif highest_score == Slytherin:
  print('You belong to Slytherin!!')

print()

print(f'Gryffindor: {Gryffindor}')
print(f'Ravenclaw: {Ravenclaw}')
print(f'Hufflepuff: {Hufflepuff}')
print(f'Slytherin: {Slytherin}')

  #After I finished I found out a cleaner way to add the points to the variables:  Hufflepuff += 2; Gryffindor += 4
    # This would save a little bit of time and in my opinion the writing will look more appealing and clear.