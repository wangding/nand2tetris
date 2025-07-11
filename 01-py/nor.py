from p1_not import Not
from p3_or import Or

def Nor(x, y):
  '''
  >>> Nor(0, 0)
  1
  >>> Nor(0, 1)
  0
  >>> Nor(1, 0)
  0
  >>> Nor(1, 1)
  0
  '''
  return Not(Or(x, y))