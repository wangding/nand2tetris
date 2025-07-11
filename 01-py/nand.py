def Nand(x, y): 
  '''
  >>> Nand(0, 0)
  1
  >>> Nand(0, 1)
  1
  >>> Nand(1, 0)
  1
  >>> Nand(1, 1)
  0
  '''
  return int(not(x and y))