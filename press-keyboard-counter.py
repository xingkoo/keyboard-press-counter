from keyboard import *
from termcolor import colored
import sys

print('开始统计按键次数,请按F10结束统计')
recorded = record(until=sys.argv[1])
totalPressed = 0
key={}
x = [chr(x) for x in range(32, 126)]
for c in x:
  key[c]=0

for k in recorded:
  totalPressed += 1
  if k.name in key:
    key[k.name]=key[k.name]+1

print('共计按键: {}次'.format(totalPressed))
i=0
for kk in key.keys():
  print(colored(str(kk).rjust(1),'red'),' ', end=' ;   ')
  if(key[kk]>0):
    print(colored(str(key[kk]).rjust(5),'green'), end=' ;   ')
  else:
    print(str(key[kk]).rjust(5), end=' ;   ')

  i=i+1
  if(i%5==0):
    print('')
  if(i==33):
    print('')
    print('')
