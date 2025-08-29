# CheckPoint Project basic Version:
  # This is an area calculator project in its most basic version proposed by Codédex for practicing the knowledge 
  # of the first 4 chapters of the Python course.
    
print('   ==============================')
print('Welcome to the Area Calculator tool 📏' )
print('   ==============================')
print()

shape = int(input('Which of the following shapes do you want to calculate the area of?: \n   1) Triangle \n   2) Rectangle \n   3) Square \n   4) Circle \n   5) Quit \n'))
if shape == 1:
  height = int(input('Enter the height: '))
  base = int(input('Enter the base: '))
  print()
  t_area = (height * base) / 2
  print(f'The area of the Triangle is: {t_area}')
  print()
       
elif shape == 2:
  lenght = int(input('Enter the length: '))
  width = int(input('Enter the width: '))
  r_area = lenght * width
  print()
  print(f'The area of the Rectangle is: {r_area}')

elif shape == 3:
  side = int(input('Enter the side measurement: '))
  s_area = side ** 2
  print()
  print(f'The area of the Square is: {s_area}')

elif shape == 4:
  radius = int(input('Enter the radius of the Circle: '))
  c_area = 3.14 * (radius ** 2)
  print()
  print(f' The area of the Circle is: {c_area}')

