from nand import Nand
from p1_not import Not

def And(x, y):
  '''
  >>> And(0, 0)
  0
  >>> And(0, 1)
  0
  >>> And(1, 0)
  0
  >>> And(1, 1)
  1
  '''
  return Not(Nand(x, y))