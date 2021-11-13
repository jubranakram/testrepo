'''
Test file for Child Branch 01
----------------------------
author: Jubran Akram
'''

def square(x):
  '''
  Square the input number
  
  Args:
  
  x (float32/64/int): input number
  
  Returns:
  
  x**2 (float32/64/int): square of the input number
  
  '''
  
  return x**2

if __name__ == '__main__':
  nums = [4, 7, 9, 11]
  nums_squared = [square(num) for num in nums]
  print(f'Input: {nums}\n')
  print(f'Output: {nums_squared}\n')
