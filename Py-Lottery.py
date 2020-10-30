import random
import numpy as np

def getResultStr(totalCount, resultCount):
  elements = [x + 1 for x in range(totalCount)]
  retStr = ''
  for i in range(resultCount):
    res = elements[random.randint(0,len(elements)-1)]
    elements.remove(res)
    retStr += ' ' + str(res)
  return retStr

lottery=['1.The Super Lotto(体彩大乐透)','2.The Double Chromosphere（福彩双色球）']

for i in range(2):
    print('%s  ' %lottery[i], end='')

try :
  note_kind=int(input('请选择种类(kind):'))
  note_number=int(input('下注数量(number)：'))
  
  if note_kind==1:
    print('%s'%lottery[note_kind-1])
    for j in range(note_number):
      print(getResultStr(35, 5),'+',getResultStr(12, 2))
  
  elif note_kind==2:
    print('%s'%lottery[note_kind-1])
    for j in range(note_number):
      print(getResultStr(33, 6),'+',getResultStr(16, 1))
  
  else:
    print('数字选项输入错误')

except ValueError:
    print('所输入的不是数字')


