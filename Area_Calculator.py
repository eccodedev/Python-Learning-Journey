#  Checkpoint project: in this version I want to ask the user if they want to make another calculation
#   before running the block of code again.

import sys
def another_calculation():
  print('Do you want to make another calculation?')
  print('   1) YES')
  print('   2) NO')

  exit = int(input())
  if exit == 2: 
    return False
  else:
    return True

def main():
  print('   ==============================')
  print('Welcome to the Area Calculator tool 📏' )
  print('   ==============================')
  print()

  flag = True
  while flag:
    shape = int(input('Which of the following shapes do you want to calculate the area of?: 👀 \n   1) 📐 Triangle \n   2) 💵 Rectangle\n   3) 🧱 Square \n   4) 📀 Circle \n   5) 🚫 Quit \n'))

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
      print()

    elif shape == 3:
      side = int(input('Enter the side measurement: '))
      s_area = side ** 2
      print()
      print(f'The area of the Square is: {s_area}')
      print()

    elif shape == 4:
      radius = int(input('Enter the radius of the Circle: '))
      c_area = 3.14 * (radius ** 2)
      print()
      print(f' The area of the Circle is: {c_area}')
      print()

    elif shape == 5:
      print()
      print('           -Goodbye 👋🍃-        ')
      print('   ==============================')
      sys.exit(0)
    
    flag = another_calculation()
if __name__ == "__main__":
  main()

print('   ==============================')
print('          -Goodbye 👋🍃-           ')
 

