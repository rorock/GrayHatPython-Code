'''
Created on Dec 6, 2015

@author: rortegon
'''
from ctypes import *
msvcrt = cdll.msvcrt
message_string = "Hello World!\n"
msvcrt.printf("Resting:%s",message_string)
