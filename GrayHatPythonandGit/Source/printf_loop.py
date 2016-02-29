from ctypes import *
import time

msvcrt = cdll.msvcrt
counter = 0
while 1:
    msvcrt.printf("Loop iteration Regina %d!\n".encode('ascii'), counter)
    #msvcrt.printf("Loop iteration Regina %d!\n", counter)
    time.sleep(2)
    counter += 1