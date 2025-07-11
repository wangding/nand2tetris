from p1_not import Not
from nand import Nand

def Or(x, y):
  '''
  >>> Or(0, 0)
  0
  >>> Or(0, 1)
  1
  >>> Or(1, 0)
  1
  >>> Or(1, 1)
  1
  '''
  return Nand(Not(x), Not(y))