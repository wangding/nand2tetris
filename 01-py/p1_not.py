from nand import Nand

def Not(x):
  '''
  >>> Not(1)
  0
  >>> Not(0)
  1
  '''
  return Nand(x, x)