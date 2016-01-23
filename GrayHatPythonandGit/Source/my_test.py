import my_debugger

debugger = my_debugger.debugger()

pid = input("Enter the PID of the process to attach to: ")

#debugger.load("C:\\WINDOWS\\system32\\calc.exe")
print ("before attach")
debugger.attach(int(pid))
print ("after attach")
printf_address = debugger.func_resolve("msvcr100.dll","printf")
print ("[*] Address of printf: 0x%016x" % printf_address)

debugger.bp_set(printf_address)
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