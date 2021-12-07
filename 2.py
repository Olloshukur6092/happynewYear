import os 
import time
from colorama import Fore, Back


filename=["file1.txt","file2.txt", "file3.txt","file4.txt", "file5.txt", "file6.txt"]

def animator(filename, delay=1, repeat=10):
	frames=[]
	for name in filename:
		with open(name, "r", encoding="utf-8") as f:
			frames.append(f.readlines())
	for i in range(repeat):
		for frame in frames:
			print(Fore.GREEN)
			print("".join(frame))
			# print(Back.LIGHTMAGENTA_EX)
			time.sleep(delay)


animator(filename, delay=0.5, repeat=10)

animator(filename, delay=0.1, repeat=20)

animator(filename, delay=2, repeat=5)
