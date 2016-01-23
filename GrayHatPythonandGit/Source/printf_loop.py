from ctypes import *
import time

msvcr100 = cdll.msvcr100
counter = 0
while 1:
    msvcr100.printf("Loop iteration %d!\n".encode('ascii'), counter)
    time.sleep(1)
    counter += 1