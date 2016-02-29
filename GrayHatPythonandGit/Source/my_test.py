import my_debugger
from my_debugger_defines import HW_EXECUTE

debugger = my_debugger.debugger()

pid = input("Enter the PID of the process to attach to: ")

#debugger.load("C:\\WINDOWS\\system32\\calc.exe")
#debugger.load("C:\\users\\rortegon\\workspace\\Gray Hat Python\\src\\printf_loop.py")
print ("before attach")
debugger.attach(int(pid))
print ("after attach")

printf_address = debugger.func_resolve("msvcrt.dll","printf")
print ("[*] Address of printf: 0x%08x" % printf_address)




#list = debugger.enumerate_threads()
#for thread in list:
#    thread_context = debugger.get_thread_context(thread)
#    print ("Dumping registers for thread ID: 0x%08x" %thread)

#this is for hardware  software breakpoints!!!!!!!!!!!!!!!
#debugger.bp_set(printf_address)

#this is for hardware breakpoints!!!!!!!!!!!11
#debugger.bp_set_hw(printf_address,1,HW_EXECUTE)

#this is for memory breakpoints
debugger.bp_set_mem(printf_address,4)
debugger.run()




#debugger.run()
#debugger.detach()

#list = debugger.enumerate_threads()
#for thread in list:
#    thread_context = debugger.get_thread_context(thread)
#    print ("Dumping registers for thread ID: 0x%08x" %thread)
#    print ("[**] EIP: 0x%08x" % thread_context.Eip)
#    print ("[**] ESP: 0x%08x" % thread_context.Esp)
#    print ("[**] EBP: 0x%08x" % thread_context.Ebp)
#    print ("[**] EAX: 0x%08x" % thread_context.Eax)
#    print ("[**] EBX: 0x%08x" % thread_context.Ebx)
#    print ("[**] ECX: 0x%08x" % thread_context.Ecx)
#    print ("[**] EDX: 0x%08x" % thread_context.Edx)
#    print ("[*] END DUMP")
    

#debugger.detach()