from p2_and import And
from p1_not import Not

def Dmux(x, sel):
  '''
  >>> Dmux(0, 0)
  (0, 0)
  >>> Dmux(1, 0)
  (1, 0)
  >>> Dmux(0, 1)
  (0, 0)
  >>> Dmux(1, 1)
  (0, 1)
  '''
  return And(x, Not(sel)), And(x, sel)