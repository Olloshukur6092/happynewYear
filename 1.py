import time
from random import randint
import os

os.system("/home/js_and_py/Music/338_Irade_Mehr=Don_Desem=94_112.bat")

for i in range(1, 45):
	print(' ')
	
s = " "

for i in range(1, 1000):
	count = randint(1, 100)
	while(count > 0):
	  s += " "
	  count -= 1
	
	if (i % 10 == 0):
	   print(s + 'Yangi Yil Bilan')
	   
	elif (i % 17 == 0): 
	   print(s + 'Olloshukur Matnazarov')
	   
	else:
	   print(s + '*')
	   
	s = ' '
	time.sleep(0.3)
