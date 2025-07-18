def dest(instruction): 
  '''
  >>> dest('DM')
  '011'
  '''
  code = {
    'M': '001',
    'D': '010',
    'DM': '011',
    'A': '100',
    'AM': '101',
    'AD': '110',
    'ADM': '111',
  }
  return code[instruction]

def comp(instruction):
  '''
  >>> comp('A+1')
  '0110111'
  >>> comp('M+1')
  '1110111'
  '''
  code = {
    'A+1': '0110111',
    'M+1': '1110111',
  }
  return code[instruction]

def jump(instruction):
  '''
  >>> jump('JNE')
  '101'
  '''
  code = {
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111',
  }
  return code[instruction]


