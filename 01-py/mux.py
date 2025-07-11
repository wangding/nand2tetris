from ad import And
from no import Not
from oor import Or

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
  s1 = And(And(x, Not(y)), Not(sel))
  s2 = And(And(x, y), Not(sel))
  s3 = And(And(Not(x), y), sel)
  s4 = And(And(x, y), sel)
  return Or(Or(Or(s1, s2), s3), s4)