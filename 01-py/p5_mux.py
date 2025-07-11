from p2_and import And
from p1_not import Not
from p3_or  import Or

def Mux(x, y, sel):
  '''
  >>> Mux(0, 0, 0)
  0
  >>> Mux(0, 1, 0)
  0
  >>> Mux(1, 0, 0)
  1
  >>> Mux(1, 1, 0)
  1
  >>> Mux(0, 0, 1)
  0
  >>> Mux(0, 1, 1)
  1
  >>> Mux(1, 0, 1)
  0
  >>> Mux(1, 1, 1)
  1
  '''
  return Or(And(x, Not(sel)), And(y, sel))