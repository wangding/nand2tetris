from no import Not
from ad import And
from oor import Or 

def Xor(x, y):
  '''
  >>> Xor(0, 0)
  0
  >>> Xor(0, 1)
  1
  >>> Xor(1, 0)
  1
  >>> Xor(1, 1)
  0
  '''
  return Or(And(Not(x), y), And(x, Not(y)))