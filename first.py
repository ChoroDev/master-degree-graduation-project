import os
import threading
import random

elems = { 
  'elem1F': '■', 'elem1E': '▢', 'elem2F': '●', 'elem2E': '○', 'elem3F': '▶', 'elem3E': '▷', 'elem4F': '◀', 'elem4E': '◁',
  'elem5F': '◆', 'elem5E': '◇', 'elem6F': '▲', 'elem6E': '△', 'elem7F': '▼', 'elem7E': '▽', 'elem8F': '▮', 'elem8E': '▯'
}
elemTypes = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], # заголовочкая строка, в которой не должно быть элементов
  ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
  ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
  ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
  ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
  ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
  ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
  ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
  ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']]

elemsStoreCount = [100, 100, 100, 200, 10, 30, 40, 50]
elemsPositions = [7, 2, 1, 3, 5, 4, 8, 6]

def mainProcess():
  os.system('clear')
  print('\n\n\n\n\n\n')
  count = '|'
  for i in range(0, 8):
    count += str(elemsStoreCount[i]) + '|'
  print(count)
  shelf = '|'
  for i in range(0, 8):
    shelf += str(elems['elem' + str(elemsPositions[i]) + 'F']) + '|'
  print(shelf)
  print('|V|V|V|V|V|V|V|V|____________________________________________________________')
  print('|___________________________________________________________                |')
  print('                                                            |V|V|V|V|V|V|V|V|')
  print('                                                            |===============| <-- start line')
  for number in range(1, 9):
    shelf = '                                                            |'
    for i in range(0, 8):
      shelf += str(elems['elem' + str(elemsPositions[i]) + elemTypes[number][i]]) + '|'
    print(shelf)
    if number == 4:
      print('                                                            |===============| <-- signal line')
    if number == 7:
      print('                                                            |===============| <-- extremal line')
    for i in range(0, 8):
      if elemTypes[number][i] == 'E' and elemTypes[number - 1][i] == 'F':
        elemTypes[number][i] = 'F'
        elemTypes[number - 1][i] = 'E'

def setInterval(func, sec):
  def func_wrapper():
    setInterval(func, sec)
    func()
  t = threading.Timer(sec, func_wrapper)
  t.start()
  return t

mainTimer = setInterval(mainProcess, 0.5)
