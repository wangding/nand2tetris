from p1_not import Not
from p2_and import And

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
  return Not(And(Not(x), Not(y)))